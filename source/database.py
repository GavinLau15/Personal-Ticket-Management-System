import psycopg2
from enum import Enum

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
    
# helper function to validate if ticket priority and status are valid entries    
def validate_enum_values(value, enum_class, field_name):
    if value not in [member.value for member in enum_class]:
        raise ValueError(f"Invalid {field_name}: {value}")

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
# TODO maybe make it return a tuple to return the create time as well
def create_ticket(cursor, title, priority, status, information) -> int:
    validate_enum_values(priority, TicketPriority, "priority")
    validate_enum_values(status, TicketStatus, "status")
    
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
    validate_enum_values(status, TicketStatus, "status")
    
    query = "UPDATE tickets SET status = %s WHERE id = %s"
    
    cursor.execute(query, (status, id))
    
# update priority of ticket with given id
def update_ticket_priority(cursor, id, priority):
    validate_enum_values(priority, TicketPriority, "priority")
    
    query = "UPDATE tickets SET priority = %s WHERE id = %s"
    
    cursor.execute(query, (priority, id))