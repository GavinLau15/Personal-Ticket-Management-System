import psycopg2
from source import database
from dotenv import load_dotenv
import os

# TODO
# scrub gitub of password perhaps
# global install vs virtual environment learn

# conn/cur default to None so finally's "is not None" checks don't raise an error if connect() 
# fails before they're ever assigned 
conn = None
cursor = None

# read the .env file and makes its values available through os.environ
load_dotenv()

# start connection object, used to connect to database
try:
    conn = psycopg2.connect(host=os.environ["DB_HOST"], 
                            dbname=os.environ["DB_NAME"],
                            user=os.environ["DB_USER"],
                            password=os.environ["DB_PASSWORD"],
                            port=os.environ["DB_PORT"])
    
    # create a cursor object, used to execute commands/queries
    cursor = conn.cursor()
    
    database.create_table(cursor)
    
    # ticket_id1 = database.create_ticket(cursor, "Ticket 1", "Low", "Assigned", "Some info")
    # ticket_id2 = database.create_ticket(cursor, "Ticket 2", "Medium", "In Progress", "Little info")
    # ticket_id3 = database.create_ticket(cursor, "Ticket 3", "High", "Resolved", "Lots of info")
    
    database.delete_ticket(cursor, 334)
    database.delete_ticket(cursor, 335)
    database.delete_ticket(cursor, 336)
    
    conn.commit()

# catches and prints any error (connection failures, bad queries, etc.) raised in try block above
except Exception as error:
    print("Error while connecting to PostgreSQL", error)
    
# guarantees the cursor and connection are closed if they were opened even if an error occured above
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()