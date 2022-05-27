def display_dash_board(students, marks):
    top_5_students = []
    least_5_students = []
    students_within_25_and_75 = []
    students_dict = dict(zip(students, marks))
    students_dict_orders = sorted(students_dict.items(), key=lambda x: x[1], reverse=True)

    print(students_dict_orders)

    for idx, i in enumerate(students_dict_orders):
        if idx < 5:
            top_5_students.append([i[0], i[1]])

        elif 4 < idx < 10:
            least_5_students.append([i[0], i[1]])

    n = len(students_dict_orders)
    percentile_1 = 25
    percentile_2 = 75

    rank_1 = percentile_1 / 100
    rank_2 = percentile_2 / 100

    rank1_n = round(rank_1 * n)
    rank2_n = round(rank_2 * n)

    for index, marks in enumerate(students_dict_orders[::-1]):
        if rank1_n <= index < rank2_n - 1:
            students_within_25_and_75.append([marks[0], marks[1]])

    print(top_5_students)
    print(least_5_students)
    print(students_within_25_and_75)

    return top_5_students, least_5_students, students_within_25_and_75


display_dash_board(
    ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8', 'student9',
     'student10'], [45, 78, 12, 14, 48, 43, 47, 98, 22, 80])
