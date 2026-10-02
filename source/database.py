import psycopg2

# create a table (if it doesn't exist already) called tickets with the following columns
# - Ticket ID (id)
# - Ticket Title (title)
# - Ticket Priority (priority)
# - Ticket Status (status)
# - Ticket Information (information)
# - Ticket Creation/Start Date (start_date)
def create_table(cursor):
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
    cursor.execute(query)

# create a ticket using a given title, priority, status and information, id and date are auto-created
# TODO make sure that values in priroty and status are valid
# TODO maybe make it return a tuple to return the create time as well
def create_ticket(cursor, title, priority, status, information) -> int:
    query = """
            INSERT INTO tickets (title, priority, status, information) 
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """
    
    cursor.execute(query, (title, priority, status, information))
    return cursor.fetchone()[0]

# retrieve ticket based on id parameter and print it
def retrieve_ticket(cursor, id):
    query = "SELECT * FROM tickets WHERE id = %s"
    
    cursor.execute(query, (id,))
    
    row = cursor.fetchone()
    
    if row is not None:
        return row
    else:
        return None

# retrieve all tickets
# TODO maybe allow specify what we are looking for, like all resolved, etc.
def retrieve_all_tickets(cursor):
    query = "SELECT * FROM tickets"
    
    cursor.execute(query)
    
    rows = cursor.fetchall()
    
    return rows

# delete ticket with given id
def delete_ticket(cursor, id):
    query = "DELETE FROM tickets WHERE id = %s"
    
    cursor.execute(query, (id,))

# update title of ticket with given id
def update_ticket_title(cursor, id, title):
    query = "UPDATE tickets SET title = %s WHERE id = %s"
    
    cursor.execute(query, (title, id))

# update information of ticket with given id
def update_ticket_info(cursor, id, information):
    query = "UPDATE tickets SET information = %s WHERE id = %s"
    
    cursor.execute(query, (information, id))
    
# update status of ticket with given id
def update_ticket_status(cursor, id, status):
    query = "UPDATE tickets SET status = %s WHERE id = %s"
    
    cursor.execute(query, (status, id))
    
# update priority of ticket with given id
# TODO make this make sure updated prio is a valid one
def update_ticket_priority(cursor, id, priority):
    query = "UPDATE tickets SET priority = %s WHERE id = %s"
    
    cursor.execute(query, (priority, id))