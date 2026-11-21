import json 
print("==============================")
print(" STUDENT RECORD MANAGEMENT ")
print("==============================")

# Store existing student records
# students = [
#     {
#         "name": "Rahul",
#         "roll_no": 101,
#         "age": 20
#     },
#     {
#         "name": "Amit",
#         "roll_no": 102,
#         "age": 21
#     },
#     {
#         "name": "Priya",
#         "roll_no": 103,
#         "age": 21
#     }
# ]

# Load student records from JSON file
try:
    with open("students.json", "r") as file:
        students = json.load(file)

# except FileNotFoundError:
#     students = []
except (FileNotFoundError, json.JSONDecodeError):
    students = []
    
# # Add new students
# number_of_students = int(input("How many students do you want to add? "))

# for i in range(number_of_students):

#     # Validate student name
#     while True:
#         name = input("Enter student name: ")

#         if name.replace(" ", "").isalpha():
#             break
#         else:
#             print("Invalid name! Please enter letters only.")

#     # Validate roll number
#     while True:
#         try:
#             roll_no = int(input("Enter roll number: "))

#             if roll_no <= 0:
#                 print("Roll number must be positive!")
#                 continue

#             break

#         except ValueError:
#             print("Please enter a valid roll number!")

#     # Enter student age
#     age = int(input("Enter student age: "))

#     # Create new student dictionary
#     new_student = {
#         "name": name,
#         "roll_no": roll_no,
#         "age": age
#     }

#     # Check duplicate roll number
#     roll_exists = False

#     for student in students:
#         if student["roll_no"] == roll_no:
#             roll_exists = True
#             break

#     if roll_exists == False:
#         students.append(new_student)
#         print("Student added successfully!")
#     else:
#         print("Roll number already exists!")

# # Display all student records
# print("\n========== ALL STUDENT RECORDS ==========")

# for student in students:
#     print("Name:", student["name"])
#     print("Roll Number:", student["roll_no"])
#     print("Age:", student["age"])
#     print("--------------------------------")

# # Search student
# search_roll = int(input("\nEnter roll number to search: "))

# found = False

# for student in students:
#     if student["roll_no"] == search_roll:

#         print("\nStudent Found!")
#         print("Name:", student["name"])
#         print("Roll Number:", student["roll_no"])
#         print("Age:", student["age"])

#         found = True
#         break

# if found == False:
#     print("Student not found!")

# # Update student record
# update_roll = int(input("\nEnter roll number to update: "))

# for student in students:
#     if student["roll_no"] == update_roll:

#         print("Student Found!")

#         # Validate new name
#         while True:
#             new_name = input("Enter new name: ")

#             if new_name.replace(" ", "").isalpha():
#                 break
#             else:
#                 print("Invalid name! Please enter letters only.")

#         new_age = int(input("Enter new age: "))

#         student["name"] = new_name
#         student["age"] = new_age

#         print("Student record updated successfully!")
#         print("Updated Student Details:", student)
#         break

# else:
#     print("Student not found!")
    
# # Delete Student Record

# delete_roll = int(input("\nEnter roll number to delete: "))

# for student in students:
#     if student["roll_no"] == delete_roll:
#         students.remove(student)
#         print("Student record deleted successfully!")
#         break
    
# else:
#     print("Student not found!")
    
# # Convert all student names to uppercase
# for student in students:
#     student["name"] = student["name"].upper()
    
# # Save student records to JSON file
# with open("students.json", "w") as file:
#     json.dump(students, file, indent=4)
    
# # Sort students by roll number
# students.sort(key=lambda student: student["roll_no"])

# # students.sort(key=lambda student: student["name"].lower(),
# # reverse=True)
# # reverse=False (default) → Ascending order.
# #reverse=True → Descending order.

# # Display final records
# print("\n========== FINAL STUDENT RECORDS ==========")

# for student in students:
#     print(student)

while True:
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "6":
        print("Thank you for using Student Management System!")
        break
    elif choice == "5":
        print("\n========== ALL STUDENT RECORDS ==========")
        
        students.sort(key=lambda student: student["roll_no"])

        for student in students:
            print(student)
            
    
    elif choice == "1":

        # Validate number of students
        while True:
            try:
                number_of_students = int(input("How many students do you want to add? "))

                if number_of_students <= 0:
                    print("Please enter a number greater than zero!")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        # Add new students
        for i in range(number_of_students):

            # Validate student name
            while True:
                name = input("Enter student name: ")

                if name.replace(" ", "").isalpha():
                    break
                else:
                    print("Invalid name! Please enter letters only.")

            # Validate roll number
            while True:
                try:
                    roll_no = int(input("Enter roll number: "))

                    if roll_no <= 0:
                        print("Roll number must be positive!")
                        continue

                    # Check duplicate roll number
                    roll_exists = False

                    for student in students:
                        if student["roll_no"] == roll_no:
                            roll_exists = True
                            break

                    if roll_exists:
                        print("Roll number already exists! Please enter another number.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid roll number!")

            # Validate student age
            while True:
                try:
                    age = int(input("Enter student age: "))

                    if age <= 0 or age > 120:
                        print("Please enter a valid age between 1 and 120!")
                        continue

                    break

                except ValueError:
                    print("Please enter numbers only!")

            # Create new student dictionary
            new_student = {
                "name": name.upper(),
                "roll_no": roll_no,
                "age": age
            }

            students.append(new_student)
            print("Student added successfully!")

        # Save updated records
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

            
    
    elif choice == "2":

        while True:
            try:
                search_roll = int(input("Enter roll number to search: "))

                if search_roll <= 0:
                    print("Roll number must be positive!")
                    continue

                break

            except ValueError:
                print("Please enter a valid roll number!")

        found = False

        for student in students:
            if student["roll_no"] == search_roll:

                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Age:", student["age"])

                found = True
                break

        if not found:
            print("Student not found!")


               
    
    elif choice == "3":

        # Validate existing roll number
        while True:
            try:
                update_roll = int(input("Enter roll number to update: "))

                if update_roll <= 0:
                    print("Roll number must be positive!")
                    continue

                break

            except ValueError:
                print("Please enter a valid roll number!")

        found = False

        for student in students:
            if student["roll_no"] == update_roll:

                print("Student Found!")

                # Validate new name
                while True:
                    new_name = input("Enter new name: ")

                    if new_name.replace(" ", "").isalpha():
                        break
                    else:
                        print("Invalid name! Please enter letters only.")

                # Validate new age
                while True:
                    try:
                        new_age = int(input("Enter new age: "))

                        if new_age <= 0 or new_age > 100:
                            print("Please enter a valid age between 1 and 100!")
                            continue

                        break

                    except ValueError:
                        print("Please enter numbers only!")

                # Validate new roll number
                while True:
                    try:
                        new_roll = int(input("Enter new roll number: "))

                        if new_roll <= 0:
                            print("Roll number must be positive!")
                            continue

                        # Check duplicate roll number
                        roll_exists = False

                        for record in students:
                            if record["roll_no"] == new_roll and record != student:
                                roll_exists = True
                                break

                        if roll_exists:
                            print("Roll number already exists! Enter another number.")
                            continue

                        break

                    except ValueError:
                        print("Please enter a valid roll number!")

                # Update student details
                student["name"] = new_name.upper()
                student["age"] = new_age
                student["roll_no"] = new_roll

                # Save updated records
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("Student record updated successfully!")
                print("Updated Student Details:", student)

                found = True
                break

        if not found:
            print("Student not found!")
            
    
    elif choice == "4":
        delete_roll = int(input("Enter roll number to delete: "))

        found = False

        for student in students:
            if student["roll_no"] == delete_roll:

                print("Student Found!")
                print("Student Details:", student)

                confirm = input("Are you sure you want to delete this record? (yes/no): ")

                if confirm.lower() == "yes":
                    students.remove(student)
                    print("Student record deleted successfully!")

                    # Save updated records
                    with open("students.json", "w") as file:
                        json.dump(students, file, indent=4)

                else:
                    print("Deletion cancelled!")

                found = True
                break

        # if found == False:
        #     print("Student not found!")

        #    # Save updated records
        #     with open("students.json", "w") as file:
        #        json.dump(students, file, indent=4)