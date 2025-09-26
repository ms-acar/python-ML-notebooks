import sqlite3
import os

def create_database():
    if os.path.exists("database.db"):
        os.remove("database.db")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn,cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Users(
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        gender VARCHAR NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE Courses(
        id INTEGER PRIMARY KEY,
        course_name VARCHAR NOT NULL,
        credit INTEGER NOT NULL,
        instructor TEXT
    )
    ''')


def insert_sample_data(cursor):

    Users = [
        (1, 'Ahmet Celik', 19, 'ahmet@example.com', 'male'),
        (2, 'Mehmet Zeki', 21, 'mehmet@example.com', 'male'),
        (3, 'Ali Önder', 20, 'ali@example.com', 'male'),
        (4, 'Zeynep Yılmaz', 18, 'zeynep@example.com', 'female'),
        (5, 'Merve Demir', 23, 'merve@example.com', 'female')
    ]

    cursor.executemany("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", Users)

    Courses = [
        (1, 'Python ML', 3, 'Atıl Samancıoğlu' ),
        (2, 'WEB Development', 2, 'Enes Bayram' ),
        (3, 'Oracle Database', 2, 'Mehmet Çelebioğlu' ),
        (4, 'Mobile Development', 4, 'Atıl Samancıoğlu' ),
        (5, 'Industrial Networking', 3, 'Cemal Taner' )
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", Courses)

def basic_sql_operations(cursor):
    #SELECT ALL
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]} NAME: {row[1]} AGE: {row[2]} EMAIL: {row[3]} GENDER: {row[4]}")

    #SELECT Columns
    cursor.execute("SELECT name, age FROM Users")
    records = cursor.fetchall()
    print(records)

    #WHERE
    cursor.execute("SELECT * FROM Users WHERE gender = 'male'")
    records = cursor.fetchall()
    print(records)

    #ORDER BY
    cursor.execute("SELECT * FROM Users ORDER BY age")
    records = cursor.fetchall()
    print(records)

def sql_insert_delete_update(conn, cursor):

    #INSERT
    cursor.execute("INSERT INTO Courses VALUES (6, 'Embedded Systems', 4, 'Coşkun Taşdemir' )")
    conn.commit()

    #UPDATE
    cursor.execute("UPDATE Courses SET credit = 3 WHERE course_name = 'Embedded Systems'")
    conn.commit()

    #DELETE
    cursor.execute("DELETE FROM Courses WHERE course_name = 'Oracle Database'")
    conn.commit()

def aggregate_func(cursor):
    #COUNT
    cursor.execute("SELECT COUNT(*) FROM Users")
    result = cursor.fetchone()
    print(result[0])
    
    #AVERAGE
    cursor.execute("SELECT Avg(age) FROM Users")
    result = cursor.fetchone()
    print(result[0])

    #MAX-MİN
    cursor.execute("SELECT MAX(age), MIN(age) FROM Users")
    result = cursor.fetchone()
    print(result)

    #GROUP BY
    cursor.execute("SELECT gender, COUNT(*) FROM Users GROUP BY gender")
    result = cursor.fetchall()
    print(result)

def main():
    print("sql with py")
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_insert_delete_update(conn, cursor)
        aggregate_func(cursor)
        conn.commit()
    except sqlite3.Error as exception:
        print(exception)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
