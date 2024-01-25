import psycopg2
import json

from colorama import Fore, Back, Style
from ConMeassageBase import error, info, warning
from db_config import host, user, password, db_name, port
from time import sleep
PATH_TO_SQL_FILE = "PyAlc/database/tables.sql"
PATH_TO_JSON_FILE = "PyAlc/database/tables.json"

"""
CREATE TABLE IF NOT EXISTS users # SQL команда для создания таблицы если она не существует
""" 


try:
    conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password
)

    # Create a new database
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"CREATE DATABASE {db_name}")
    except Exception as e:
        match e:
            case psycopg2.errors.DuplicateDatabase:
                warning("Database already exists.")
            case psycopg2.errors.InFailedSqlTransaction:
                error(f"Error while creating database: {e}")
            case _:
                error(f"Error while creating database: {e}")
    else:
        info("Database created successfully.")

    # Close the cursor and connection
    cur.close()
    conn.close()


        # Connect to the newly created database
except Exception as e:
    match e:
        case psycopg2.Error:
            error(f"Connecting to the database: {e}")
        case _: 
            error(f"Connecting to the database: {e}")
    cur.close()
    conn.close()

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
                # Create the tables
                create_table_query = '''
                CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(40),
                    user_weight FLOAT,
                    height FLOAT,
                    gender VARCHAR(10),
                    age INTEGER
                )
                '''
                try:
                    cursor.execute(create_table_query)
                    conn.commit()
                except Exception as e:
                    match e:
                        case psycopg2.errors.DuplicateTable:
                            error("Table already exists.")
                        case psycopg2.errors.InFailedSqlTransaction:
                            error(f"Error while creating table: {e}")
                        case _:
                            error(f"Error while creating table: {e}")
                else:
                    info("Users table created successfully.")
except Exception as e:
    match e:
        case psycopg2.Error:
            error(f"Connecting to the database: {e}")
        case _: 
            error(f"Connecting to the database: {e}")

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
                create_drinks_table_query = '''
                CREATE TABLE drinks (
                    drink_id SERIAL PRIMARY KEY,
                    drink_name VARCHAR(40),
                    drink_type VARCHAR(20),
                    drink_abv FLOAT,
                    drink_base VARCHAR(20) DEFAULT 'neutral',
                    drink_volumes INTEGER[]
                )
                '''
                try:
                    cursor.execute(create_drinks_table_query)
                    conn.commit()
                except Exception as e:
                    match e:
                        case psycopg2.errors.DuplicateTable:
                            error("Table already exists.")
                        case psycopg2.errors.InFailedSqlTransaction:
                            error(f"Error while creating table: {e}")
                        case _:
                            error(f"Error while creating table: {e}")
                else:
                    info("Drinks table created successfully.")
                
except Exception as e:
    match e:
        case psycopg2.Error:
            error(f"Connecting to the database: {e}")
        case _: 
            error(f"Connecting to the database: {e}")


# Connect to the database
try:
    with psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
        port=port
    ) as conn:
        # Create a cursor object
        conn.autocommit = True
        try:
            with conn.cursor() as cursor:
                # Get the table names
                cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
                table_names = [row[0] for row in cursor.fetchall()]

                # Create a dictionary to store table names and column names
                data = {}
                for table_name in table_names:
                    # Get the column names for each table
                    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                    column_names = [row[0] for row in cursor.fetchall()]
                    data[table_name] = column_names

                # Write the data to a JSON file
                with open(PATH_TO_JSON_FILE, "w") as json_file:
                    json.dump(data, json_file, indent=4)
        except Exception as e:
            match e:
                case psycopg2.Error:
                    error(f"Error while retrieving table and column names: {e}")
                case _:
                    error(f"Error while retrieving table and column names: {e}")
        else:
            info("Table and column names retrieved successfully.")
            
except Exception as e:
    match e:
        case psycopg2.Error:
            error(f"Connecting to the database: {e}")
        case _: 
            error(f"Connecting to the database: {e}")
