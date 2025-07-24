student_marks = {
    "omkar": 85,
    "mayank": 92,
    "rahul": 78,
    "abhishek": 90,
    "chutka": 88
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
