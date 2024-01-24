"""

# From db_main.py

try:
    with psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
        port=port
    ) as conn:
        with conn.cursor() as cursor:
            # Save tables to file
            try:
                with open(PATH_TO_SQL_FILE, 'w') as file:
                    cursor.copy_expert("COPY (SELECT * FROM users) TO STDOUT WITH CSV HEADER", file)
                    cursor.copy_expert("COPY (SELECT * FROM drinks) TO STDOUT WITH CSV HEADER", file)
                    conn.commit()
            except Exception as e:
                error(f"Error while saving tables to file: {e}")
            else:
                info("Tables saved to file successfully.")

except Exception as e:
    match e:
        case psycopg2.Error:
            error("Connecting to the database:", e)




"""