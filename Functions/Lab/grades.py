grade = float(input())


def grade_scores():
    if 2 < grade <= 2.99:
        return "Fail"
    elif 2.99 < grade <= 3.49:
        return "Poor"
    elif 3.49 < grade <= 4.49:
        return "Good"
    elif 4.49 < grade <= 5.49:
        return "Very Good"
    elif 5.49 < grade <= 6.00:
        return "Excellent"


print(grade_scores())

