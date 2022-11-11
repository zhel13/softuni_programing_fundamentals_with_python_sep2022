courses = input()
course_dictionary = {}
while courses != "end":
    course, name = courses.split(" : ")
    if not course in course_dictionary:
        course_dictionary[course] = []
    course_dictionary[course].append(name)
    courses = input()
for key, value in course_dictionary.items():
    print(f"{key}: {len(course_dictionary[key])}")
    for student in course_dictionary[key]:
        print(f"-- {''.join(student)}")