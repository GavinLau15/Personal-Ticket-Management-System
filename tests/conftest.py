import pytest
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def cursor():
    
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ["DB_PORT"]
    )
    
    cur = conn.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                information TEXT NOT NULL,
                start_date DATE NOT NULL DEFAULT CURRENT_DATE)
                """)
    
    conn.commit()

    # pass cur to each test, everything before yield runs before test
    yield cur

    conn.rollback()  # undo any inserts the test made
    cur.close()
    conn.close()