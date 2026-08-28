import psycopg2


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
    
    # create table named tickets
    # cur.execute("""CREATE TABLE IF NOT EXISTS tickets (
    #     id SERIAL PRIMARY KEY,
    #     title VARCHAR(255) NOT NULL,
    #     description TEXT,
    #     status VARCHAR(50) NOT NULL,
    #     priority VARCHAR(50) NOT NULL,
    #     creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    # );
    # """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                ticketid INT PRIMARY KEY, 
                information TEXT NOT NULL
                )
                """)
    
    cur.execute("""
                INSERT INTO tickets (ticketid, information)
                VALUES (%s, %s)
                """,
                (15, "testing"))
    
    cur.execute("""
                INSERT INTO tickets (ticketid, information)
                VALUES (118, 'test')
                """)
    
    insertIntoTickets = "INSERT INTO tickets (ticketid, information) VALUES (%s, %s)"
    parameters = (17, "testing")
    
    cur.execute(insertIntoTickets, parameters)
    
    # cur.execute("""INSERT INTO tickets (id, title, description, status, priority, creation_date) 
    #             VALUES 
    #             (DEFAULT, 'Plotter supplies', 'Run script to get supplies for monthly accounting.', 'In Progress', 'Low', DEFAULT);
    #     """)
    
    
    
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