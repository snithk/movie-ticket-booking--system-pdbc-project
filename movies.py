from dp import get_connection
def view_all_movies():
    connection=get_connection()
    cursor=connection.cursor()
    query="select * from movies"
    cursor.execute(query)
    result=cursor.fetchall()
    print("Movie ID    Movie Name   Language   Release Date    Duration    Genre")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])
def search_movie_by_name(name):
    connection=get_connection()
    cursor=connection.cursor()
    query=f"select * from movies where title='{name}'"
    cursor.execute(query)
    result=cursor.fetchall()
    print("Movie ID    Movie Name   Language   Release Date    Duration    Genre")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])
def filter_movies_by_language(language):
    connection=get_connection()
    cursor=connection.cursor()
    query=f"select * from movies where language='{language}'"
    cursor.execute(query)
    result=cursor.fetchall()
    print("Movie ID    Movie Name   Language   Release Date    Duration    Genre")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])
def filter_movies_by_genre(genre):
    connection=get_connection()
    cursor=connection.cursor()
    query=f"select * from movies where genre like '%{genre}%'"
    cursor.execute(query)
    result=cursor.fetchall()
    print("Movie ID    Movie Name   Language   Release Date    Duration    Genre")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])
def filter_movies_by_rating(rating):
    connection=get_connection()
    cursor=connection.cursor()
    query=f"select * from movies where rating='{rating}'"
    cursor.execute(query)
    result=cursor.fetchall()
    print("Movie ID    Movie Name   Language   Release Date    Duration    Genre")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])




