#Timofey
import random

N = int(input("Введіть кількість елементів N: "))
a = [random.randint(1, 100) for _ in range(N)]

print("Згенерований список a:", a)

P = int(input("Введіть значення P: "))
if 1 <= P <= N:
    елемент = a.pop(P-1)
    a.insert(0, елемент)
    print("Оновлений список a:", a)
else:
    print("P поза допустимим діапазоном!")