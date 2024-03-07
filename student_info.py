#initilization of empty list and dictionary
students_list = []
students_dict = {}

#promote user to enter their name, age and grade
students_name = input("enter student name: ")
students_age = input("enter student age: ")
students_grade = input("enter student grade: ")
students_list.append(students_name)
students_dict[students_name] = {"age":students_age, "grade":students_grade}
print("student information added successfully!")
print(students_dict)

#disply students information
search_student = input("enter student name to search or simply enter to skip: ")
if search_student in students_dict:
    print(f"student found!: {students_dict[search_student]}")
else:
    print("student not found!")

#remove student information
remove_student = input("enter the name of student to remove or smiply enter to skip: ")
if remove_student in students_dict:
    students_name.remove(remove_student)
    del students_dict[remove_student]
    print("student removed!")
else:
    print("student not found!")







