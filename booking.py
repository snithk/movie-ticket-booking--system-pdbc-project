from dp import get_connection
def book_ticket():
    """
    Function to book a ticket for a user.
    This function will handle the booking process, including checking availability,
    reserving the ticket, and confirming the booking.
    """
    # Check ticket availability
    connection = get_connection()
    cursor = connection.cursor(buffered=True)
    t=input("enter the threater name")
    m=input("enter the movie name")
    time=input("enter the time")
    cursor.execute(f"""SELECT s.show_id,s.price,s.available_seats
                        FROM theatres t
                        JOIN screens sc ON t.theatre_id = sc.theatre_id
                        JOIN shows s ON sc.screen_id = s.screen_id
                        JOIN movies m ON s.movie_id = m.movie_id
                        WHERE t.theatre_name = %s AND s.show_time = %s AND m.title = %s """, (t, time, m))
    w = cursor.fetchone()
    print(w)

    if w is None:
        print("Show not found!")
        return

    show_id = w[0]
    price = w[1]
    available_seats = w[2]

    customer_id=int(input("enter the customer id")) 
    no_of_tickets=int(input("enter the number of tickets"))
    if no_of_tickets <= 0 or no_of_tickets > available_seats:
        print("Invalid ticket count or insufficient seats!")
        return
    total_amount=price*no_of_tickets 
    insert_query = f"INSERT INTO bookings(customer_id, show_id, seats, total_amount, status) VALUES({customer_id}, {show_id}, {no_of_tickets}, {total_amount}, 'Confirmed')"   
    cursor.execute(insert_query)
    update_query = f"UPDATE shows SET available_seats = available_seats - %s WHERE show_id = %s AND available_seats >= %s"
    cursor.execute(update_query, (no_of_tickets, show_id, no_of_tickets))
    theater_name=f"update shows set available_seats=available_seats-{no_of_tickets} where threater_name='{t}' "
    print("Ticket booked successfully!")
    connection.commit()


def view_bookings():
    """
    Function to view all bookings for a user.
    This function will retrieve and display the booking details for the user.
    """
    connection = get_connection()
    cursor = connection.cursor(buffered=True)
    customer_id=int(input("enter the customer id")) 
    cursor.execute(f"SELECT * FROM bookings WHERE customer_id = %s and status = 'Confirmed'", (customer_id,))
    bookings = cursor.fetchall()

    if not bookings:
        print("No bookings found!")
        return

    print("Your Bookings:")
    for booking in bookings:
        print(f"Booking ID: {booking[0]}, Show ID: {booking[2]}, Seats: {booking[3]}, Total Amount: {booking[4]}, Status: {booking[5]}")
def cancel_booking():
    """
    Function to cancel a booking for a user.
    This function will handle the cancellation process, including updating the booking status
    and restoring the available seats for the show.
    """
    connection = get_connection()
    cursor = connection.cursor(buffered=True)
    booking_id=int(input("enter the booking id")) 
    cursor.execute(f"SELECT show_id, seats FROM bookings WHERE booking_id = %s AND status = 'Confirmed'", (booking_id,))
    booking = cursor.fetchone()

    if booking is None:
        print("Booking not found or already cancelled!")
        return

    show_id = booking[0]
    seats_to_restore = booking[1]

    # Update the booking status to 'Cancelled'
    update_booking_query = f"UPDATE bookings SET status = 'Cancelled' WHERE booking_id = %s"
    cursor.execute(update_booking_query, (booking_id,))

    # Restore the available seats for the show
    restore_seats_query = f"UPDATE shows SET available_seats = available_seats + %s WHERE show_id = %s"
    cursor.execute(restore_seats_query, (seats_to_restore, show_id))

    print("Booking cancelled successfully!")
    connection.commit()