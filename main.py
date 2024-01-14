import mysql.connector
from datetime import datetime, timedelta

# connect to mysql 

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'thaalibiya',
    database = 'reservation_sys'
)

mycursor = connection.cursor()

def make_reservation(id, guest_name, check_in_date, check_out_date) :
    query = "INSERT INTO reservation VALUES (%s, %s, %s, %s)"
    
    data = (id, guest_name, check_in_date, check_out_date)
    mycursor.execute(query, data)
    connection.commit()
    print("reservation made successfully !")

def view_reservation() :
    query = "SELECT * FROM reservation"
    mycursor.execute(query)
    reservations = mycursor.fetchall()
    
    for i in reservations :
        print(f"ID : {i[0]}, Guest : {i[1]}, Check_in  : {i[2]}, Check_out : {i[3]}")
    
#exemple 
make_reservation('147258369', 'jhon Doe', '2024-01-14', '2024-01-18')

view_reservation()

mycursor.close()
connection.close()