# ------------------------------------------------- #
# Title: Assignment05.py
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Romulo Reyes Jr, 02/23/2026/, Created Script
# ------------------------------------------------- #

import json
from pathlib import Path

# -------------------- Constants -------------------- #
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

#This makes the file automatically save in the same folder as the Python script#
FILE_NAME: str = str(Path(__file__).parent / "Enrollments.json")


# -------------------- Variables -------------------- #
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# -------------------- Processing -------------------- #

# Load existing data from file at program start
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
 
except FileNotFoundError:
    print("\n\033[91mWarning:Enrollments.json not found. Starting with empty data!\033[0m")
except json.JSONDecodeError:
    print("\n\033[91mWarning:File is empty or contains invalid JSON.\033[0m")
except Exception as e:
    print("\n\033[91mWarning::Unexpected error occurred while reading file:\033[0m", e)
    file.close()


# Main Program Loop
while True:
    print(MENU)
    menu_choice = input("Enter your choice [1-4]: ").strip()

    # Option 1 – Register Student
    if menu_choice == "1":
        try:
            student_first_name = input("Enter student's first name: ").strip()
            if not all(c.isalpha() or c.isspace() for c in student_first_name):
                raise ValueError("First name must contain only letters.")

        except ValueError as e:
            print("\n\033[91mError:", e, "\033[0m")
            continue

        try:
            student_last_name = input("Enter student's last name: ").strip()
            if not all(c.isalpha() or c.isspace() for c in student_last_name):
                raise ValueError("Last name must contain only letters.")

        except ValueError as e:
            print("\n\033[91mError:", e, "\033[0m")
            continue

        course_name = input("Enter course name: ").strip()

        student_data = {
            "FirstName": student_first_name,
            "LastName": student_last_name,
            "Course": course_name
        }

        students.append(student_data)
        print("Student registered successfully.\n")

    # Option 2 – Show Current Data
    elif menu_choice == "2":
        print("\n--- Current Enrollments ---")
        for row in students:
            print(f"{row['FirstName']}, {row['LastName']}, {row['Course']}")
        print()

    # Option 3 – Save Data to File
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()

            print("\nData successfully saved to file.")
            print("Saved Data:")
            for row in students:
                print(f"{row['FirstName']}, {row['LastName']}, {row['Course']}")
            print()

        except TypeError:
            print("Type error occurred while writing to file.")
        except Exception as e:
            print("Unexpected error occurred while writing file:", e)

    # Option 4 – Exit
    elif menu_choice == "4":
        print("Program exiting...Goodbye!")
        break

    else:
        print("Invalid option, please choose between 1-4.\n")