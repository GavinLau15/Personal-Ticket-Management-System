import pytest
import psycopg2
from dotenv import load_dotenv
from source.database import create_table
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
    
    cursor = conn.cursor()
    
    create_table(cursor)
    
    conn.commit()

    # pass cur to each test, everything before yield runs before test
    yield cursor

    conn.rollback()  # undo any inserts the test made
    cursor.close()
    conn.close()