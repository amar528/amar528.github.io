if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks.get(query_name)
    if not marks:
        raise IndexError('That student does not exist.')

    print('%.2f' % (sum(marks) / len(marks)))
