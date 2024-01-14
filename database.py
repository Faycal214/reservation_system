import mysql.connector

def create_db():
    mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'thaalibiya'
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE TABLE reservation_sys")
    
def create_tab ():
    mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'thaalibiya',
    database = 'reservation_sys'
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute("""
        CRAETE TABLE reservation (
        id VARCHAR(10) PRIMARY KEY ,
        client_name VARCHAR(10) NOT NULL,
        check_in_date DATE NOT NULL ,
        check_out_date DATE NOT NULL
    )
    """)

create_db()
create_tab()