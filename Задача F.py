#Timofey
def calculate_average(grades):
    return round(sum(grades) / len(grades), 2)

def get_last_name_and_grades():
    N = int(input("Введіть кількість учнів: "))
    students = []

    for _ in range(N):
        data = input("Введіть прізвище та оцінки (математика, фізика, інформатика): ").strip().split()
        surname = data[0]
        grades = list(map(int, data[1:]))
        average = calculate_average(grades)
        students.append((surname, grades, average))

    students.sort(key=lambda student: (-student[2], student[0]))

    print("Результати:")
    for surname, grades, average in students:
        print(f"{surname} {' '.join(map(str, grades))} {average}")

get_last_name_and_grades()
