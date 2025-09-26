import sqlite3
import os


def create_database():
    if os.path.exists("database.db"):
        os.remove("database.db")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER)
        ''')


def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Sample data inserted successfully")

def questions():
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Chicago'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''

def answers(cursor):

    #1) Bütün kursların bilgilerini getirin

    cursor.execute("SELECT * FROM Courses")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]} COURSE NAME: {row[1]} INSTRUCTOR: {row[2]} CREDITS: {row[3]}")

    #2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin

    cursor.execute("SELECT course_name, instructor FROM Courses")
    result = cursor.fetchall()
    print(result)

    #3) Sadece 21 yaşındaki öğrencileri getirin

    cursor.execute("SELECT * FROM Students WHERE age = 21")
    result = cursor.fetchall()
    print(result)

    #4) Sadece Chicago'da yaşayan öğrencileri getirin

    cursor.execute("SELECT * FROM Students WHERE city = 'Chicago'")
    result = cursor.fetchall()
    print(result)

    #5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin

    cursor.execute("SELECT * FROM Courses WHERE instructor = 'Dr. Anderson'")
    result = cursor.fetchall()
    print(result)

    #6) Sadece ismi 'A' ile başlayan öğrencileri getirin

    cursor.execute("SELECT * FROM Students WHERE name LIKE 'A%'")
    result = cursor.fetchall()
    print(result)

    #7) Sadece 3 ve üzeri kredi olan dersleri getirin

    cursor.execute("SELECT * FROM Courses WHERE credits >= 3")
    result = cursor.fetchall()
    print(result)

    print("----------------------")

    #1) Öğrencileri alphabetic şekilde dizerek getirin

    cursor.execute("SELECT * FROM Students ORDER BY name ASC")
    print(cursor.fetchall())

    #2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin

    cursor.execute("SELECT * FROM Students WHERE age > 20 GROUP BY name")
    print(cursor.fetchall())

    #3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin

    cursor.execute("SELECT * FROM Students WHERE city = 'New York' OR city = 'Chicago'")
    print(cursor.fetchall())

    #4) Sadece 'New York' ta yaşamayan öğrencileri getirin

    cursor.execute("SELECT name FROM Students WHERE city <> 'Chicago'")
    print(cursor.fetchall())

def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        answers(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    main()