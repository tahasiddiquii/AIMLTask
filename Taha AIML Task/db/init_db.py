import psycopg2
from psycopg2 import sql

def create_tables():
    """Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS videos (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            transcription TEXT NOT NULL,
            tags VARCHAR(255)
        )
        """,
    )
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=tahadb user=postgres password=root host=localhost")
        cur = conn.cursor()
        
        # Execute each command to create tables
        for command in commands:
            print(f"Executing command: {command}")
            cur.execute(command)
        
        # Close communication with the PostgreSQL database server
        cur.close()
        
        # Commit the changes
        conn.commit()
        print("Tables created successfully")
    except psycopg2.DatabaseError as error:
        print(f"Error: {error}")
    finally:
        # Close the connection
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
