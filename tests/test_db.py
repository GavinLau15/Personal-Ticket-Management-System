import pytest
import psycopg2
from source.database import create_ticket, update_ticket_title, update_ticket_priority, update_ticket_status, update_ticket_info

def test_create_ticket(cursor):
    create_ticket(cursor, "Outlook Setup", "Low", "In Progress", "Set up Outlook account")
    
    query = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE title = %s
            """
    cursor.execute(query, ("Outlook Setup",))
    
    row = cursor.fetchone()
    
    assert row is not None
    assert isinstance(row[0], int)
    assert row[1] == "Outlook Setup"
    assert row[2] == "Low"
    assert row[3] == "In Progress"
    assert row[4] == "Set up Outlook account"

def test_update_ticket_title(cursor):
    create_ticket(cursor, "Desktop Crashing", "Medium", "Assigned", "Desktop is frequently crashing")
    
    query = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE title = %s
            """
    
    cursor.execute(query, ("Desktop Crashing",))
    
    row = cursor.fetchone()
    
    id = row[0]
    
    update_ticket_title(cursor, id, "OS Crashing")
    
    newQuery = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE id = %s
            """
    cursor.execute(newQuery, (id,))
    
    newRow = cursor.fetchone()
    
    assert newRow[1] == "OS Crashing"
    
def test_update_ticket_priority(cursor):
    create_ticket(cursor, "Can't find email", "Medium", "Assigned", "Cannot find specific email sent a week ago")
    
    query = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE title = %s
            """
    
    cursor.execute(query, ("Can't find email",))
    
    row = cursor.fetchone()
    
    id = row[0]
    
    update_ticket_priority(cursor, id, "High")
    
    newQuery = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE id = %s
            """
    cursor.execute(newQuery, (id,))
    
    newRow = cursor.fetchone()
    
    assert newRow[2] == "High"
    
def test_update_ticket_info(cursor):
    create_ticket(cursor, "Set up firewall", "High", "In Progress", "Set up firewall for plotters")
    
    query = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE title = %s
            """
    
    cursor.execute(query, ("Set up firewall",))
    
    row = cursor.fetchone()
    
    id = row[0]
    
    update_ticket_info(cursor, id, "Configure SMTP/DNS for printers/plotters")
    
    newQuery = """
            SELECT id, title, priority, status, information
            FROM tickets
            WHERE id = %s
            """
    cursor.execute(newQuery, (id,))
    
    newRow = cursor.fetchone()
    
    assert newRow[4] == "Configure SMTP/DNS for printers/plotters"
    
# def test_retrieve_ticket(cursor):
    

# def test_delete_row(cursor):
#     create_ticket(cursor, "Set up firewall", "High", "In Progress", "Set up firewall for plotters")
    
    
            
    
    # ticket3 = 
    # ticket4 = create_ticket(cur, "Excel crashing", "Low", "Assigned", "Excel crashing when opening specific file")
    # ticket5 = create_ticket(cur, "Assign VPC", "Low", "Resolved", "Assign a VPC for remote use")
    # ticket5 = 
    # ticket7 = create_ticket(cur, "Printer jamming", "Low", "Resolved", "Printer is jamming when printing large loads")