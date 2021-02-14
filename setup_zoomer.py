from mysql_utils import connect, create_database
from utils import getjoinposn, update_pass


def main():
    conn, cursor = connect(SETUP=True)

    print("Creating database...")
    create_database(cursor)
    cursor.execute("USE ZOOMER;")

    print("creating tables...")
    setup_passwords(cursor)

    getjoinposn()


def setup_passwords(cursor):
    try:
        cursor.execute(
            "CREATE TABLE passwords( "
            "subject varchar(10), "
            "id varchar(10), "
            "password varchar(10))"
        )
    except Exception as err:
        print(f"An error has occured: {err}")

    path = input("Enter the location of the file with passwords:")
    update_pass(path)


if __name__ == "__main__":
    main()
