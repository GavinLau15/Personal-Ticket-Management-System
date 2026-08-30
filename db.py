import psycopg2

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

def update_ticket_info():
    return

def delete_ticket():
    return

def 