import psycopg2
import sys

def upload_to_db(file_path, title, db_params):
    # Connect to your postgres DB
    conn = psycopg2.connect(db_params)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Read HTML content from file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Execute the insert command
    cur.execute("INSERT INTO notebooks (title, content) VALUES (%s, %s)", (title, html_content))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    file_path = sys.argv[1]
    title = sys.argv[2]
    db_params = "dbname=mydatabase user=postgres password=yourpassword host=localhost port=5432"
    upload_to_db(file_path, title, db_params)
