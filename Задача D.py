#Timofey
N = int(input("Введіть кількість студентів: "))

for _ in range(N):
    data = input("Введіть прізвище та оцінки (математика, фізика, інформатика): ").split()
    name = data[0]
    scores = list(map(int, data[1:]))
    avg_score = sum(scores) / len(scores)

    print(f"{name} {avg_score:.2f}")