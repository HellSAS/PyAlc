import json
import psycopg2

from ConMeassageBase import error, info, warning
from db_config import host, user, password, db_name, port

"""!!!НЕ РАБОТАЕТ, НЕ ТРОГАЙ!!!"""

PATH_TO_JSON_FILE = "./database/tables.json"

# Load table data from table.json
with open(PATH_TO_JSON_FILE, 'r') as file:
    table_data = json.load(file)

def add_row(table_name, values):
            try:
                with conn.cursor() as cursor:
                    query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(values))})"
                    cursor.execute(query, values)
                    info("Row added successfully.")
            except Exception as e:
                error(f"Error adding row: {e}")

        # Function to update a row in the table
def update_row(table_name, column_name, new_value, condition):
    try:
        with conn.cursor() as cursor:
            query = f"UPDATE {table_name} SET {column_name} = %s WHERE {condition}"
            cursor.execute(query, (new_value,))
            info("Row updated successfully.")
    except Exception as e:
        error(f"Error updating row: {e}")

# Function to delete a row from the table
def delete_row(table_name, condition):
    try:
        with conn.cursor() as cursor:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            cursor.execute(query)
            info("Row deleted successfully.")
    except Exception as e:
        error(f"Error deleting row: {e}")
        
        
def print_menu():
            print("1. Add a row")
            print("2. Update a row")
            print("3. Delete a row")
            print("4. Exit")

def get_table_name():
    return input("Enter the table name: ")

def get_values():
    values = input("Enter the values (comma-separated): ")
    return [value.strip() for value in values.split(",")]

def get_column_name():
    return input("Enter the column name: ")

def get_new_value():
    return input("Enter the new value: ")

def get_condition():
    return input("Enter the condition: ")

def handle_add_row():
    table_name = get_table_name()
    values = get_values()
    add_row(table_name, values)

def handle_update_row():
    table_name = get_table_name()
    column_name = get_column_name()
    new_value = get_new_value()
    condition = get_condition()
    update_row(table_name, column_name, new_value, condition)

def handle_delete_row():
    table_name = get_table_name()
    condition = get_condition()
    delete_row(table_name, condition)
    
def main():
        while True:
            print_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                handle_add_row()
            elif choice == "2":
                handle_update_row()
            elif choice == "3":
                handle_delete_row()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


try:
    with psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
        port=port
    ) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            main()

            # Commit the changes and close the connection
            conn.commit()

        if __name__ == "__main__":
            main()


except Exception as e:
    match e:
        case psycopg2.Error:
            error("Connecting to the database:", e)
        case _: 
            error("Connecting to the database:", e)


# Commit the changes and close the connection
conn.commit()
