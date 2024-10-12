#Timofey
import random

N = int(input("Введіть кількість елементів N: "))
a = [random.randint(1, 100) for _ in range(N)]

print("Згенерований список a:", a)

P = int(input("Введіть значення P: "))
результат = [str(x) for x in a if x != P]

print("Список без значень P:", ' '.join(результат))