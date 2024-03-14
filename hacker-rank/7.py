if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    sorted_distinct_grades = sorted(list({s[1] for s in students}))
    second_lowest_grade = sorted_distinct_grades[1]

    second_lowest_graded_names = [s[0] for s in students if s[1] == second_lowest_grade]
    second_lowest_graded_names.sort()

    for student in second_lowest_graded_names:
        print(student)
