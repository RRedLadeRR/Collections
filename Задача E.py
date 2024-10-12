#Timofey
def calculate_averages(N, students):
    total_math = 0
    total_physics = 0
    total_informatics = 0

    for grades in students:
        total_math += grades[0]
        total_physics += grades[1]
        total_informatics += grades[2]

    average_math = total_math / N
    average_physics = total_physics / N
    average_informatics = total_informatics / N

    return round(average_math, 2), round(average_physics, 2), round(average_informatics, 2)

def get_last_name_and_grades():
    N = int(input("Введіть кількість студентів: "))
    students = []

    for _ in range(N):
        data = input("Введіть прізвище та оцінки (математика, фізика, інформатика): ").strip().split()
        grades = list(map(int, data[1:]))
        students.append(grades)

    averages = calculate_averages(N, students)

    print(f"Середній бал по математиці: {averages[0]}")
    print(f"Середній бал по фізиці: {averages[1]}")
    print(f"Середній бал по інформатиці: {averages[2]}")

get_last_name_and_grades()
