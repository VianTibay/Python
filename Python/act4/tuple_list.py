import os
import json
from operator import itemgetter

filename = "students.json"
records = []
if os.path.exists(filename):
    with open(filename, "r+") as file:
        records = json.load(file)

while True:
    print("\nMenu:")
    print("1. Show All Students Record")
    print("2. Order by Last Name")
    print("3. Order by Grade")
    print("4. Add Record")
    print("5. Edit Record")
    print("6. Delete Record")
    print("7. Save File")
    print("8. Save As File")
    print("9. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("\nStudent Records:")
        for record in records:
            final_grade = round((record['class_standing'] * 0.6) + (record['major_exam'] * 0.4), 2)
            print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, "
                  f"Class Standing: {record['class_standing']}, Exam: {record['major_exam']}, "
                  f"Final Grade: {final_grade}")
    elif choice == "2":
        records.sort(key=lambda x: x['name'][1])
    elif choice == "3":
        records.sort(key=lambda x: round((x['class_standing'] * 0.6) + (x['major_exam'] * 0.4), 2), reverse=True)
    elif choice == "4":
        student_id = input("Enter Student ID (6 digits): ")
        if len(student_id) != 6 or not student_id.isdigit():
            print("Invalid Student ID!")
            continue
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        records.append({
            "id": student_id,
            "name": (first_name, last_name),
            "class_standing": class_standing,
            "major_exam": major_exam
        })
    elif choice == "5":
        student_id = input("Enter Student ID to edit: ")
        for record in records:
            if record["id"] == student_id:
                record["class_standing"] = float(input("Enter New Class Standing Grade: "))
                record["major_exam"] = float(input("Enter New Major Exam Grade: "))
                print("Record Updated!")
                break
        else:
            print("Record not found!")
    elif choice == "6":
        student_id = input("Enter Student ID to delete: ")
        for record in records:
            if record["id"] == student_id:
                records.remove(record)
                print("Record Deleted!")
                break
        else:
            print("Record not found!")
    elif choice == "7":
        with open(filename, "w") as file:
            json.dump(records, file, indent=4)
        print("Records saved successfully.")
    elif choice == "8":
        new_filename = input("Enter new filename: ")
        with open(new_filename, "w") as file:
            json.dump(records, file, indent=4)
        print("Records saved successfully to new file.")
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
