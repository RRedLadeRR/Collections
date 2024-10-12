#Timofey
import random

N = int(input("Введіть кількість елементів N: "))

a = [random.randint(1, 100) for _ in range(N)]

print("Згенерований список a:", a)

P = int(input("Введіть значення P: "))
if 1 <= P <= N:
    a.pop(P-1)
    print("Список після видалення елемента з індексом P-1:", a)
else:
    print("P поза допустимим діапазоном!")

Q, K = map(int, input("Введіть значення Q і K через пробіл: ").split())

if 1 <= Q <= len(a) + 1:
    a.insert(Q-1, K)
    print("Список після вставки елемента K перед елементом Q-1:", a)
else:
    print("Q поза допустимим діапазоном!")

print("Оновлений список a:", ' '.join(map(str, a)))