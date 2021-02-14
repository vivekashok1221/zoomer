import mysql.connector
from mysql.connector import errorcode, errors


def connect(SETUP=False):
    try:
        db = "ZOOMER" if not SETUP else None
        conn = mysql.connector.connect(
            user="root", host="localhost", passwd="isgsql", database=db
        )
    except mysql.connector.errors.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found.\n" "run python zoomer.py --setup")
            raise SystemExit
        else:
            print("An error has occured: {err}")
            raise SystemExit

    else:
        return conn, conn.cursor()


def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE ZOOMER;")
    except errors.Error as err:
        print(f"An error has occured while creating the database: {err}")
    else:
        cursor.execute("USE ZOOMER;")
        print("Database created")


def insert_records(cursor, records):
    try:
        cursor.execute("Insert into passwords values(%s, %s, %s)", records)
    except errors.Error as err:
        print(f"An error occured while inserting values: {err}")
    except Exception as err:
        print(f"An error occured:{err}")
