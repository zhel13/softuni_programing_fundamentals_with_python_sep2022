from statistics import median
num_input = int(input())
student_grades = {}

for _ in range(num_input):
    student = input()
    grade = float(input())
    if not student in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for student, grade in student_grades.items():
    if median(grade) >= 4.5:
        print(f"{student} -> {median(grade):.2f}")





