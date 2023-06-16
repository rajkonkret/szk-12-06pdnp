import sqlite3

# baza sqlite - baza sql w pliku

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(2,'Python',200);
    '''
    cursor = sql_connection.cursor()
    print("Baza została podłaczona...")

    cursor.execute(insert)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

# Baza została podłaczona...
# Baza została zamknieta
