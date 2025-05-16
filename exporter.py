
import sqlite3
import os

def export_sqlite_to_sql():
    # Connect to SQLite database
    conn = sqlite3.connect('community.db')
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Open output file
    with open('community_dump.sql', 'w') as f:
        # Iterate through tables
        for table in tables:
            table_name = table[0]

            # Get table schema
            cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            create_table = cursor.fetchone()[0]

            # Write create table statement
            f.write(f"{create_table};\n\n")

            # Get all data
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            # Write insert statements
            for row in rows:
                values = ','.join([f"'{str(value)}'" if value is not None else 'NULL' for value in row])
                f.write(f"INSERT INTO {table_name} VALUES({values});\n")
            f.write("\n")

    conn.close()
    print(f"Database exported to community_dump.sql")

if __name__ == "__main__":
    export_sqlite_to_sql()