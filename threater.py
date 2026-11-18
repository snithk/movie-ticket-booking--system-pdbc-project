from dp import get_connection
def get_theatre_show_details():
    connection=get_connection()
    cursor=connection.cursor()
    query=""" select t.theatre_name, m.title, sc.screen_name
             , s.show_time, s.price from theatres t
              join screens sc on t.theatre_id=sc.theatre_id
              join shows s on sc.screen_id = s.screen_id
              join movies m on s.movie_id=m.movie_id"""
    cursor.execute(query)
    result=cursor.fetchall()
    print("Theatre name      Movie Name   screen _name   Show Time \t\t price")
    for row in result: 
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

# -- SELECT s.show_id,m.title,t.theatre_id,t.theatre_name,t.location,s.show_time 
# -- FROM theatres t
# -- JOIN screens sc ON t.theatre_id = sc.theatre_id
# -- JOIN shows s ON sc.screen_id = s.screen_id
# -- JOIN movies m ON s.movie_id = m.movie_id
# -- where m.title="Pushpa 2" and t.theatre_name="PVR Cinemas" and s.show_time ='18:00:00' ;

