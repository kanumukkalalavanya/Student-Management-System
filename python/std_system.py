import mysql.connector


# 1. DATABASE CONNECTION

def connection_database():
    return mysql.connector.connect(
        host="localhost",
        database="student_database",
        user="root",
        password="1812"
    )


# 2. ADD STUDENT

def add_student():

    conn = None
    cursor = None

    try:
        conn = connection_database()
        cursor = conn.cursor()

        roll_number = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))
        phone_no = input("Enter Phone Number: ")
        email_id = input("Enter Email ID: ")

        query = """
        INSERT INTO student_data
        (roll_number, name, age, marks, phone_no, email_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            roll_number,
            name,
            age,
            marks,
            phone_no,
            email_id
        )

        cursor.execute(query, values)
        conn.commit()

        print("Student added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


# 3. DISPLAY ALL STUDENTS

def display_students():

    conn = None
    cursor = None

    try:
        conn = connection_database()
        cursor = conn.cursor()

        query = "SELECT * FROM student_data"

        cursor.execute(query)

        records = cursor.fetchall()

        if records:
            print("\n----- STUDENT RECORDS -----")

            for row in records:
                print(row)

        else:
            print("No student records found.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


# 4. SEARCH STUDENT

def search_student():

    conn = None
    cursor = None

    try:
        conn = connection_database()
        cursor = conn.cursor()

        roll_number = int(input("Enter Roll Number: "))

        query = """
        SELECT * FROM student_data
        WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))

        record = cursor.fetchone()

        if record:
            print("\nStudent Details:")
            print(record)

        else:
            print("Student not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


# 5. UPDATE STUDENT

def update_student():

    conn = None
    cursor = None

    try:
        conn = connection_database()
        cursor = conn.cursor()

        roll_number = int(input("Enter Roll Number: "))
        new_marks = float(input("Enter New Marks: "))

        query = """
        UPDATE student_data
        SET marks = %s
        WHERE roll_number = %s
        """

        cursor.execute(query, (new_marks, roll_number))

        conn.commit()

        if cursor.rowcount > 0:
            print("Student details updated successfully!")

        else:
            print("Student not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


# 6. DELETE STUDENT

def delete_student():

    conn = None
    cursor = None

    try:
        conn = connection_database()
        cursor = conn.cursor()

        roll_number = int(input("Enter Roll Number: "))

        query = """
        DELETE FROM student_data
        WHERE roll_number = %s
        """

        cursor.execute(query, (roll_number,))

        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")

        else:
            print("Student not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()


# 7. MAIN MENU

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You! Exiting Student Management System.")
        break

    else:
        print("Invalid Choice! Please try again.")