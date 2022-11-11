data = input()
courses = {}

while ":" in data:
    student_name, id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][id] = student_name
    data = input()
searched_course = data
searched_course_name = searched_course.split("_")
searched_course = " ".join(searched_course_name)
for course_name in courses:
    if course_name == searched_course:
        for student_id, name in courses[course_name].items():
            print(f"{name} - {student_id}")
