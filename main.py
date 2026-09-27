import psycopg2
from source import database
from dotenv import load_dotenv
import os
from enum import Enum

# TODO
# scrub gitub of password perhaps
# global install vs virtual environment learn

# the 3 different priority options for a ticket
# pass .value into database.py functions - DB column is plain TEXT, not a Postgres enum type
class TicketPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

# the 3 different status options for a ticket
# pass .value into database.py functions - DB column is plain TEXT, not a Postgres enum type
class TicketStatus(Enum):
    ASSIGNED = "Assigned"
    INPROGRESS = "In Progress"
    RESOLVED = "Resolved"

# conn/cur default to None so finally's "is not None" checks don't raise an error if connect() 
# fails before they're ever assigned 
conn = None
cur = None

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
    cur = conn.cursor()
    
    database.create_table(cur)
    
    database.create_ticket(cur, "Ticket 1", TicketPriority.LOW.value, TicketStatus.ASSIGNED.value, "Some info")
    database.create_ticket(cur, "Ticket 2", TicketPriority.MEDIUM.value, TicketStatus.INPROGRESS.value, "Little info")
    database.create_ticket(cur, "Ticket 3", TicketPriority.HIGH.value, TicketStatus.RESOLVED.value, "Lots of info")
    
    conn.commit()

# catches and prints any error (connection failures, bad queries, etc.) raised in try block above
except Exception as error:
    print("Error while connecting to PostgreSQL", error)
    
# guarantees the cursor and connection are closed if they were opened even if an error occured above
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()