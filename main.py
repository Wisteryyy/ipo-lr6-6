import random

k = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]

u = set()

for c in k:
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            u.add((c[i], c[j]))

l = list(u)
print("Уникальные пары:", l)

m = int(input("Введите целое число: "))

w = 0
for p in l:
    if (p[0] + p[1]) < m:
        w += 1

print("Количество пар, чья сумма меньше заданного пользователем значения:", w)