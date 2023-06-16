import sqlite3

# baza sqlite - baza sql w pliku

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłaczona...")
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

# Baza została podłaczona...
# Baza została zamknieta
