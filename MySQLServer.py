#importing libraries

import os
import sys
import mysql.connector 


#database name
DB_NAME = "alx_book_store"

#
def main():
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("Mukangu!994", "")
    port = int(os.getenv("MYSQL_PORT", "3306"))

    conn = None
    try:
        conn = connect(host=host, user=user, password=password, port=port)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        print(f"Database '{DB_NAME}' created successfully!")
    except Error as e:
        print(f"ERROR: Could not create database '{DB_NAME}'. Details: {e}")
        sys.exit(1)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
