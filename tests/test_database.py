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
    # with pytest.raises(ValueError, match="Ticket not found"):
    
    assert row is None
    
    

# def test_retrieve_ticket_not_found(cursor):
#     database.create_ticket(cursor, "Assign VPC", "Low", "Resolved", "Assign a VPC for remote use")
    
#     retrieveResult = database.retrieve_ticket(cursor, 67)
    
#     assert retrieveResult == None

# # test updating the status of a ticket with given id
# def test_update_ticket_status(cursor):
#     database.create_ticket(cursor, "Excel crashing", "Low", "Assigned", "Excel crashing when opening specific file")
    
#     query = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE title = %s
#             """
    
#     cursor.execute(query, ("Excel crashing",))
    
#     row = cursor.fetchone()
    
#     id = row[0]
    
#     database.update_ticket_status(cursor, id, "Resolved")
    
#     newQuery = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE id = %s
#             """

#     cursor.execute(newQuery, (id,))
    
#     newRow = cursor.fetchone()
    
#     assert newRow[3] == "Resolved"

# def test_update_ticket_title(cursor):
#     database.create_ticket(cursor, "Desktop Crashing", "Medium", "Assigned", "Desktop is frequently crashing")
    
#     query = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE title = %s
#             """
    
#     cursor.execute(query, ("Desktop Crashing",))
    
#     row = cursor.fetchone()
    
#     id = row[0]
    
#     database.update_ticket_title(cursor, id, "OS Crashing")
    
#     newQuery = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE id = %s
#             """
#     cursor.execute(newQuery, (id,))
    
#     newRow = cursor.fetchone()
    
#     assert newRow[1] == "OS Crashing"
    
# def test_update_ticket_priority(cursor):
#     database.create_ticket(cursor, "Can't find email", "Medium", "Assigned", "Cannot find specific email sent a week ago")
    
#     query = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE title = %s
#             """
    
#     cursor.execute(query, ("Can't find email",))
    
#     row = cursor.fetchone()
    
#     id = row[0]
    
#     database.update_ticket_priority(cursor, id, "High")
    
#     newQuery = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE id = %s
#             """
#     cursor.execute(newQuery, (id,))
    
#     newRow = cursor.fetchone()
    
#     assert newRow[2] == "High"
    
# def test_update_ticket_info(cursor):
#     database.create_ticket(cursor, "Set up firewall", "High", "In Progress", "Set up firewall for plotters")
    
#     query = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE title = %s
#             """
    
#     cursor.execute(query, ("Set up firewall",))
    
#     row = cursor.fetchone()
    
#     id = row[0]
    
#     database.update_ticket_info(cursor, id, "Configure SMTP/DNS for printers/plotters")
    
#     newQuery = """
#             SELECT id, title, priority, status, information
#             FROM tickets
#             WHERE id = %s
#             """
#     cursor.execute(newQuery, (id,))
    
#     newRow = cursor.fetchone()
    
#     assert newRow[4] == "Configure SMTP/DNS for printers/plotters"
    

# def test_delete_row(cursor):
#     database.create_ticket(cursor, "Printer jamming", "Low", "Resolved", "Printer is jamming when printing large loads")
    
#     query = """
#             SELECT id, priority, status, information
#             FROM tickets
#             WHERE title = %s
#             """
            
#     cursor.execute(query, ("Printer jamming",))
    
#     row = cursor.fetchone()
    
#     id = row[0]
    
#     database.delete_ticket(cursor, id)
    
#     assert retrieve_ticket(cursor, id) == None
    
            

    # ticket5 = create_ticket(cur, "Assign VPC", "Low", "Resolved", "Assign a VPC for remote use")
    # ticket7 = create_ticket(cur, "Printer jamming", "Low", "Resolved", "Printer is jamming when printing large loads")