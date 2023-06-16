import sqlite3

import sqlite3

# baza sqlite - baza sql w pliku

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE SqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);'''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza została podłaczona...")
    cursor.executescript(sql_script)

    # cursor.execute(query)
    # sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

# Baza została podłaczona...
# Baza została zamknieta
