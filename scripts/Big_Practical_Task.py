
students = [
    {'name': "Hermione", 'grades': [95, 90, 97]},
    {'name': "Harry", 'grades': [80, 90, 78]},
    {'name': "Ron", 'grades': [60, 70, 64]},
    {'name': "Draco", 'grades': [60, 75, 70]},
    {'name': "Poco", 'grades': []} #тестовый перс
]


def calculate_average(grades):
    if grades:
        return sum(grades) / len(grades)
    return 0


def show_students(students):
    print("[Show_students]: -------------")

    for student in students:
        grades = student['grades']
        average = calculate_average(grades)
        status = "Успешен" if average >= 75 else "Отстает"

        print(
            f"Студент: {student['name']}\n"
            f"Средний балл: {average:.2f}\n"
            f"Статус: {status}\n"
        )


def average_grades(students):
    grades_sum = []

    for student in students:
        grades = student['grades']
        average = calculate_average(grades)
        grades_sum.append(average)

    return sum(grades_sum) / len(students)


def min_grades_remove(students):
    min_grade = students[0]

    for student in students:
        grades = student['grades']

        if calculate_average(grades) < calculate_average(min_grade['grades']):
            min_grade = student

    students.remove(min_grade)


show_students(students)
print(f"Общий средний балл: {average_grades(students):.2f}")

students.append({'name': 'Jinny', 'grades': [96, 86, 92]})

print("\nПосле добавления студента:")
show_students(students)
print(f"Общий средний балл: {average_grades(students):.2f}")

min_grades_remove(students)

print("\nПосле удаления студента с самым низким средним баллом:")
show_students(students)
print(f"Общий средний балл: {average_grades(students):.2f}")
