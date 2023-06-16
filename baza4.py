import sqlite3

# baza sqlite - baza sql w pliku

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    select = '''
    SELECT * FROM software;
    '''
    update = '''
    UPDATE software SET price = 2000 WHERE id = 1;'''
    delete = '''
    DELETE FROM software WHERE id = 1'''
    cursor = sql_connection.cursor()
    print("Baza została podłaczona...")

    for row in cursor.execute(select):  # (1, 'Python', 200.0)
        print(row)
    # update na bazie danych
    # cursor.execute(update)

    # delete - usunięcie rekordu z bazy danych
    cursor.execute(delete)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Błąd podczas podłączania bazy", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

# Baza została podłaczona...
# Baza została zamknieta
