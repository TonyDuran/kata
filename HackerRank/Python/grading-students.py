try:
    from raw_input import input
except ImportError:
    pass

def gradingStudents(grades):
    curved_grades = list()
    for grade in grades:
        if grade < 38:
            curved_grades.append(grade)
            continue
        else:
            next_multiple = ((grade - (grade % 5) + 5))
            if (next_multiple - grade) < 3:
                curved_grades.append(next_multiple)
            else:
                curved_grades.append(grade)
    return curved_grades



if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(*result,sep="\n")