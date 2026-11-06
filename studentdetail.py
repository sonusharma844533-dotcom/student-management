
import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()


# Add student
def add_student():
    print("\n--- Add Student ---")
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
            (sid, name, age, course, marks)
        )
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Student ID already exists!")


# Display students
def display_students():
    print("\n--- Student Records ---")
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No student records found.")
    else:
        for student in records:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Age: {student[2]} | "
                f"Course: {student[3]} | "
                f"Marks: {student[4]}"
            )


# Search student
def search_student():
    print("\n--- Search Student ---")
    sid = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?", (sid,)
    )
    student = cursor.fetchone()

    if student:
        print("Student Found:", student)
    else:
        print("Student not found!")


# Update student
def update_student():
    print("\n--- Update Student ---")
    sid = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?", (sid,)
    )

    if cursor.fetchone():
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = float(input("Enter New Marks: "))

        cursor.execute("""
            UPDATE students
            SET name = ?, age = ?, course = ?, marks = ?
            WHERE id = ?
        """, (name, age, course, marks, sid))

        conn.commit()
        print("Student updated successfully!")
    else:
        print("Student not found!")


# Delete student
def delete_student():
    print("\n--- Delete Student ---")
    sid = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id = ?", (sid,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")


# Main menu
while True:
    print("\n================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        display_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        update_student()

    elif choice == '5':
        delete_student()

    elif choice == '6':
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

conn.close()
