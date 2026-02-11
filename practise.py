import os
import sqlite3

def create_database():
    if os.path.exists('students.db'):
        os.remove('students.db')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY, 
        name VARCHAR NOT NULL, 
        age INTEGER,
        email VARCHAR UNIQUE, 
        city VARCHAR )
    ''')

    cursor.execute('''
    CREATE TABLE Courses (
        id INTEGER PRIMARY KEY, 
        course_name VARCHAR NOT NULL, 
        instructor TEXT, 
        credits INTEGER )
    ''')

def insert_sample_data(cursor):
    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
         ]

    cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', students)

    courses = [
        (1,'Python Programming','Dr. Anderson', 3),
        (2,'Web Development','Prof. Wilson', 4),
        (3,'Data Science','Dr. Taylor', 3),
        (4,'Mobile Apps','Prof. Garcia', 2),
    ]
    cursor.executemany('INSERT INTO Courses VALUES (?, ?, ?, ?)', courses)
    print('Sample data inserted successfully')

def basic_sql_operations(cursor):
    # 1-) SELECT ALL
    print("-" * 35 + "Select All" + "-" * 35)
    cursor.execute('SELECT * FROM Students')
    records = cursor.fetchall()
    for row in records:
        # print(row) -> tuple şeklinde gelir
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mail: {row[3]}, City: {row[4]}") # -> daha güzel gözükür.

    # 2-) SELECT COLUMNS
    print("-" * 33 + " Select Columns " + "-" * 33)
    cursor.execute('SELECT name,age FROM Students')
    records = cursor.fetchall()
    for row in records:
        print(f"Name: {row[0]}, Age: {row[1]}")

    # 3-) WHERE CLAUSE
    print("-" * 34 + " Where Clause " + "-" * 34)
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mail: {row[3]}, City: {row[4]}")

    # 4-) WHERE CLAUSE 2
    print("-" * 33 + " Where Clause 2 " + "-" * 33)
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mail: {row[3]}, City: {row[4]}")

    # 5-) ORDER BY ASC
    print("-" * 36 + " ORDER BY " + "-" * 36)
    cursor.execute("SELECT name,age FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(f"Name: {row[0]}, Age: {row[1]}")

    # 5-) ORDER BY DESC
    print("-" * 35 + " ORDER BY 2 " + "-" * 35)
    cursor.execute("SELECT name,age FROM Students ORDER BY age DESC")
    records = cursor.fetchall()
    for row in records:
        print(f"Name: {row[0]}, Age: {row[1]}")

    # 6-) LIMIT
    print("-" * 37 + " LIMIT " + "-" * 37)
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Mail: {row[3]}, City: {row[4]}")


def sql_changing_operations(conn, cursor): # UPDATE - DELETE - INSERT
    # 1-) INSERT
    cursor.execute('INSERT INTO Students VALUES (6, "Frank Miller" , 24, "frank@gmail.com","Miami" )')
    conn.commit()

    cursor.execute('INSERT INTO Students VALUES (7, "Hank Cutler" , 23, "hank@gmail.com","Chicago" )')
    conn.commit()

    # 2-) UPDATE
    cursor.execute('UPDATE Students SET city = "Istanbul" WHERE city = "New York"')
    conn.commit()

    # 3-) DELETE
    cursor.execute('DELETE FROM Students WHERE id = 6')
    conn.commit()

def aggregate_functions(cursor):
    # 1-) COUNT
    print("-" * 37 + " COUNT " + "-" * 37)
    cursor.execute('SELECT COUNT (*) FROM Students')
    result = cursor.fetchone()
    print(result[0])
    #result = cursor.fetchall()
    #print(result[0][0])


    # 2-) AVERAGE / AVG
    print("-" * 22 + " Agregate Functions AVERAGE / AVG " + "-" * 23)
    cursor.execute('SELECT AVG(age) FROM Students')
    result = cursor.fetchone()
    print(result[0])

    # 3-) MAX
    print("-" * 28 + " Agregate Functions MAX " + "-" * 29)
    cursor.execute('SELECT MAX(age) FROM Students')
    result = cursor.fetchone()
    print(result[0])

    # 4-) MIN
    print("-" * 28 + " Agregate Functions MIN " + "-" * 28)
    cursor.execute('SELECT MIN(age) FROM Students')
    result = cursor.fetchone()
    print(result[0])

    # 5-) MAX / MIN
    print("-" * 25 + " Agregate Functions MAX / MIN " + "-" * 25)
    cursor.execute('SELECT MAX(age),MIN(age) FROM Students')
    result = cursor.fetchone()
    max_age , min_age = result
    print(f"Max Age: {max_age}, Min Age: {min_age}")
    #print(result[0], result[1], sep = " and ")

    # 6-) GROUP BY
    print("-" * 25 + " Agregate Functions GROUP BY " + "-" * 26)
    cursor.execute('SELECT city , COUNT(*) FROM Students GROUP BY city')
    result = cursor.fetchall()
    print(result)


def answers(cursor):
    print("-" * 37 + " ANSWERS " + "-" * 37)

    # Question 1
    print("-" * 36 + " ANSWERS 1 " + "-" * 36)
    cursor.execute("SELECT * FROM Courses")
    get_all_courses = cursor.fetchall()
    for row in get_all_courses:
        print(row[0], row[1], row[2], row[3], sep = " --> ")

    # Question 2
    print("-" * 36 + " ANSWERS 2 " + "-" * 36)
    cursor.execute("SELECT course_name, instructor FROM Courses")
    get_course_instructors = cursor.fetchall()
    for row in get_course_instructors:
        print(row[0], row[1] , sep = " --> ")

    # Question 3
    print("-" * 36 + " ANSWERS 3 " + "-" * 36)
    cursor.execute('SELECT name, age FROM Students WHERE age = 21')
    records = cursor.fetchall()
    for row in records:
        print(row[0], row[1] , sep = " --> ")

    # Question 4
    print("-" * 36 + " ANSWERS 4 " + "-" * 36)
    cursor.execute('SELECT name, age FROM Students WHERE city = "Chicago"')
    records = cursor.fetchall()
    for row in records:
        print(row[0], row[1] , sep = " --> ")

    # Question 5
    print("-" * 36 + " ANSWERS 5 " + "-" * 36)
    cursor.execute('SELECT instructor, course_name FROM Courses WHERE instructor = "Dr. Anderson"')
    records = cursor.fetchall()
    for row in records:
        print(row[0], row[1] , sep = " --> ")

    # Question 6
    print("-" * 36 + " ANSWERS 6 " + "-" * 36)
    cursor.execute('SELECT name FROM Students WHERE name LIKE "A%"')
    records = cursor.fetchall()
    for row in records:
        print(row[0])

    # Question 7
    print("-" * 36 + " ANSWERS 7 " + "-" * 36)
    cursor.execute('SELECT course_name FROM Courses WHERE credits >= 3')
    records = cursor.fetchall()
    for row in records:
        print(row[0])

    # Question 8
    print("-" * 36 + " ANSWERS 8 " + "-" * 36)
    cursor.execute('SELECT name FROM Students ORDER BY Name')
    records = cursor.fetchall()
    for row in records:
        print(row[0])

    # Question 9
    print("-" * 36 + " ANSWERS 9 " + "-" * 36)
    cursor.execute('SELECT name FROM Students WHERE age > 20 ORDER BY Name')
    records = cursor.fetchall()
    for row in records:
        print(row[0])

    # Question 10
    print("-" * 36 + " ANSWERS 10 " + "-" * 36)
    cursor.execute('SELECT name FROM Students WHERE city = "New York" OR city = "Chicago"')
    records = cursor.fetchall()
    for row in records:
        print(row[0])

    # Question 11
    print("-" * 36 + " ANSWERS 11 " + "-" * 36)
    cursor.execute('SELECT name FROM Students WHERE city != "New York"')
    records = cursor.fetchall()
    for row in records:
        print(row[0])


def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_changing_operations(conn, cursor)
        aggregate_functions(cursor)
        answers(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == "__main__":
    main()