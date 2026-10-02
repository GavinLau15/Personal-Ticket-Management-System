import pytest
import psycopg2
from source import database

# test creating a table
# def test_create_table():
#     assert

# test creating a ticket
def test_create_ticket(cursor):
    ticket_id = database.create_ticket(cursor, "Outlook Setup", "Low", "In Progress", "Set up Outlook")
    
    cursor.execute("""
                   SELECT title, priority, status, information
                   FROM tickets 
                   WHERE id = %s
                   """, 
                   (ticket_id,))
    
    row = cursor.fetchone()
    
    assert row is not None
    assert row[0] == "Outlook Setup"
    assert row[1] == "Low"
    assert row[2] == "In Progress"
    assert row[3] == "Set up Outlook"

# test the succesful retrieval of a ticket
def test_retrieve_ticket(cursor):
    ticket_id = database.create_ticket(cursor, "Set up firewall", "High", "In Progress", "Set up firewall for plotters")
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row is not None
    assert row[0] == ticket_id
    assert row[1] == "Set up firewall"
    assert row[2] == "High"
    assert row[3] == "In Progress"
    assert row[4] == "Set up firewall for plotters"

# test the retrieval of a ticket that does not exist
def test_retrieve_ticket_not_found(cursor):
    row = database.retrieve_ticket(cursor, 999999)
    
    assert row is None

# test the retrieval of all tickets 
def test_retrieve_all_tickets(cursor):
    database.create_ticket(cursor, "Provision user", "Low", "Assigned", "Provide a machine for a new user")
    database.create_ticket(cursor, "Assign VPC", "Medium", "In Progress", "Assign a VPC for remote use")
    database.create_ticket(cursor, "Change password", "High", "Resolved", "Change password")
    
    rows = database.retrieve_all_tickets(cursor)
    
    assert len(rows) == 3

# test deleting a ticket
def test_delete_ticket(cursor):
    ticket_id = database.create_ticket(cursor, "Temporary ticket", "Low", "Assigned", "Test ticket")
    
    database.delete_ticket(cursor, ticket_id)
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row is None
    
# test updating the title of a ticket
def test_update_ticket_title(cursor):
    ticket_id = database.create_ticket(cursor, "Excel crashing", "Low", "Assigned", "Excel crashing when opening specific file")
    
    database.update_ticket_title(cursor, ticket_id, "MS Excel Crashing")
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row[0] == ticket_id
    assert row[1] == "MS Excel Crashing"
    assert row[2] == "Low"
    assert row[3] == "Assigned"
    assert row[4] == "Excel crashing when opening specific file"

# test updating the information of a ticket
def test_update_ticket_info(cursor):
    ticket_id = database.create_ticket(cursor, "Desktop Crashing", "Medium", "Assigned", "Desktop is frequently crashing")
    
    database.update_ticket_info(cursor, ticket_id, "PC crashes frequently")
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row[0] == ticket_id
    assert row[1] == "Desktop Crashing"
    assert row[2] == "Medium"
    assert row[3] == "Assigned"
    assert row[4] == "PC crashes frequently"

# test updating the status of a ticket
def test_update_ticket_status(cursor):
    ticket_id = database.create_ticket(cursor, "Printer jamming", "Low", "In Progress", "Printer is jamming when printing large loads")
    
    database.update_ticket_status(cursor, ticket_id, "Resolved")
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row[0] == ticket_id
    assert row[1] == "Printer jamming"
    assert row[2] == "Low"
    assert row[3] == "Resolved"
    assert row[4] == "Printer is jamming when printing large loads"

# test updating the priority of a ticket
def test_update_ticket_priority(cursor):
    ticket_id = database.create_ticket(cursor, "Can't find email", "Medium", "Assigned", "Cannot find specific email sent a week ago")
    
    database.update_ticket_priority(cursor, ticket_id, "High")
    
    row = database.retrieve_ticket(cursor, ticket_id)
    
    assert row[0] == ticket_id
    assert row[1] == "Can't find email"
    assert row[2] == "High"
    assert row[3] == "Assigned"
    assert row[4] == "Cannot find specific email sent a week ago"