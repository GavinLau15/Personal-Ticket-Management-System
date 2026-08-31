import psycopg2

# create a table called tickets
# TODO add a username column
def create_table(cur):
    query = """
                CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY, 
                title TEXT NOT NULL, 
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                information TEXT NOT NULL,
                start_date DATE NOT NULL DEFAULT CURRENT_DATE
                )
                """
    cur.execute(query)

# create a ticket using a given title, priority, status and information, id and date are auto-created
def create_ticket(cur, title, priority, status, information):
    query = "INSERT INTO tickets (title, priority, status, information) VALUES (%s, %s, %s, %s)"
    
    cur.execute(query, (title, priority, status, information))

# retrieve ticket based on id parameter and print it
def retrieve_ticket(cur, id):
    query = "SELECT * FROM tickets WHERE id = %s"
    
    cur.execute(query, (id,))
    
    row = cur.fetchone()
    
    if row is not None:
        print(row)
    else:
        print("Not found")

# retrieve all tickets
def retrieve_all_tickets(cur):
    query = "SELECT * FROM tickets"
    
    cur.execute(query)
    
    rows = cur.fetchall()
    
    return rows

# update information of ticket with given id
def update_ticket_info(cur, id, information):
    query = "UPDATE tickets SET information = %s WHERE id = %s"
    
    cur.execute(query, (information, id))

# delete ticket with given id
def delete_ticket(cur, id):
    query = "DELETE FROM tickets WHERE id = %s"
    
    cur.execute(query, (id,))
