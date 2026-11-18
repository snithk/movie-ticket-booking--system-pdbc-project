from dp import get_connection
from movies import *
from threater import *
from booking import *
while True:
    print("1. View Movies")
    print("2. View Theatre Show Details")
    print("3. Book Ticket")
    print("4. View Bookings")
    print("5. cancel the ticket")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("1. View All Movies")
        print("2. Search Movie by Name")
        print("3. Filter Movies by Language")
        print("4. Filter Movies by Genre")
        print("5. Filter Movies by Rating")
        sub_choice = input("Enter your choice: ")
        while True:
            if sub_choice == '1':
                view_all_movies()
                break
            elif sub_choice == '2':
                name = input("Enter movie name: ")
                
                search_movie_by_name(name)
                
                break
            elif sub_choice == '3':
                language = input("Enter language: ")
                filter_movies_by_language(language)
                break
            elif sub_choice == '4':
                genre = input("Enter genre: ")
                filter_movies_by_genre(genre)
                break
            elif sub_choice == '5':
                rating = input("Enter rating: ")
                filter_movies_by_rating(rating)
                break
            elif sub_choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")
                break
            
    elif choice == '2':
        get_theatre_show_details()
    elif choice == '3':
        book_ticket()
    elif choice == '4':
        view_bookings()
    elif choice == '5':
        cancel_booking()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
