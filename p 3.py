#=====================================
# project: Students data oraganizer
# project.3 Collection Manipulator
#=====================================

# List to store all student record dictionaries

students = []

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    print()

    match choice:
        case 1:
            # Add Student
            print("Enter student details:")
            student_id = int(input("Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            subjects_input = input("Subjects (comma-separated): ")

           
            # Store student data in a dictionary
            student = {
                "identity": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "dob":dob,
                "subjects": subjects_input                            
            }
            
            students.append(student)
            print("\nStudent added successfully!")

        case 2:
            # Display All Students
            if not students:
                print("No records found.")
            else:
                print("--- Display All Students ---")
                for stu in students:
                   print(f"Student ID: {stu['identity']} | Name: {stu['name']} | Age: {stu['age']} | Grade: {stu['grade']} | DOB: {stu['dob']} | Subjects: {stu['subjects']}")
                print()
                

        case 3:
            # Update Student Information
            search_id = int(input("Enter Student ID to update: "))
            found = False
            
            for stu in students:
                if stu["identity"] == student_id:
                   while True:
                        print("1. Update name")
                        print("2. Update Age")
                        print("3. Update grade")
                        print("4. Update dob")
                        print("5. Update subject_input")
                        print("6. back")
                        c = int(input("Enter your choice: "))
                        match c:
                            case 1:
                                name = input('enter update name: ')
                                stu['name'] = name
                            case 2:
                                age = input('enter update age: ')
                                stu['age'] = age
                            case 3:
                                grade = input('enter update grade: ')
                                stu['grade'] = grade
                            case 4:
                                dob = input('enter update dob: ')
                                stu['dob'] = dob
                            case 5:
                                subjects = input('enter update subjects: ')
                                stu['subjects'] = subjects
                            case 6:break
                            case _:print("invalid choise.....")
                   found = True
                   print("Update Record Success.......")
                    
            if found == False:
                print("No Record Found....")
            print()
         
                    
        case 4:
            # Delete Student using 'del'
            student_id =int( input("Enter Delete Student ID: "))
            found = False
            
            for stu in students:
                if stu["identity"] == student_id:
                    students.remove(stu)
                    found = True
                    print("Delete Record Success.......")
                    
                    
            if found == False:
                print("No Record Found....")
            print() 
        case 5:
            # Display Unique Subjects Offered across all students
            all_subjects = set()
            for stu in students:
                all_subjects.update(stu["subjects"])
            if all_subjects:
                print("--- Unique Subjects Offered ---")
                print("all_subject")
               
            else:
                print("No subjects found.")

        case 6:
            # Exit Message
            print("Thank you for using the Student Data Organizer! Goodbye.")
            break

        case _:
            print("Invalid Choice...")
