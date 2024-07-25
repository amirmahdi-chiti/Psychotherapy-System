import psycopg2
from psycopg2 import sql

DATABASE_URL = "postgres://postgres:changeme@localhost/"

def create_database():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'Psychotherapy'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('Psychotherapy')))
        print("Database 'Psychotherapy' created.")
    else:
        print("Database 'Psychotherapy' already exists.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
