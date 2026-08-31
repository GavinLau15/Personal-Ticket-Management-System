import pytest
import psycopg2

@pytest.fixture
def cursor():
    
    conn = psycopg2.connect(
        host="localhost",
        dbname="Personal Ticket Management",
        user="postgres",
        password="chinesedragon",
        port=5432
    )
    
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
    
    conn.commit()

    # pass cur to each test, everything before yield runs before test
    yield cur

    conn.rollback()  # undo any inserts the test made
    cur.close()
    conn.close()