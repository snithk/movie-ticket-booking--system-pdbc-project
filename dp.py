from mysql.connector import connect
def get_connection():
    connection=connect(
        host="localhost",
        user="root",
        password="mysql",
        database="ticketsbooking"
    )
    return connection
