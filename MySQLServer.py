""" Creates the database alx_book_store """

import mysql.connector

def main():
    try:
        # Connect to MySQL server and create the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mukangu!994" 
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database alx_book_store created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
