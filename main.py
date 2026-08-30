import psycopg2
from enum import Enum

class TicketPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    
class TicketStatus(Enum):
    ASSIGNED = "Assigned"
    INPROGRESS = "In Progress"
    RESOLVED = "Resolved"

conn = None
cur = None

# start connection object, connects to database
try:
    conn = psycopg2.connect(host="localhost", 
                            dbname="Personal Ticket Management", 
                            user="postgres", 
                            password="chinesedragon", 
                            port=5432)
    
    # create a cursor object, used to execute commands/queries
    cur = conn.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY, 
                title TEXT NOT NULL, 
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                information TEXT NOT NULL,
                start_date DATE NOT NULL DEFAULT CURRENT_DATE
                )
                """)
    
    # retrieve ticket based on id
    retrieveTicketQuery = "SELECT * FROM tickets WHERE id = %s"
    id1 = (1,)
    
    cur.execute(retrieveTicketQuery, id1)
    
    row = cur.fetchone()
    
    if row is not None:
        print(row)
    else:
        print("Not found")
        
    updateTicketInfoQuery = "UPDATE tickets SET information = %s WHERE id = %s"
    testParams = ("test the update function", 1)
    cur.execute(updateTicketInfoQuery, testParams)
    
    # editing info of ticket
    
    # deleting a ticket
    
    #changing priority of ticket
    
    # save transactions to database
    conn.commit()
    
except Exception as error:
    print("Error while connecting to PostgreSQL", error)
    
# close the cursor and connection if they were opened
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()