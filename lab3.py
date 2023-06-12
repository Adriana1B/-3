n = 6
r = 5
# Обчислення чисельника
P1 = 1
for i in range(1, n+1):
    P1 *= i
# Обчислення знаменника
P2 = 1
for i in range(1, n-r+1):
    P2 *= i
# Обчислення кількості розміщень без повторень
A = P1 / P2
# Виведення результату
print("----1-----")
print("Кількість усіх розміщень без повторень:", A)
print("----2-----")
def compute_stirling(n): #обч числа Стірлінга другого роду для заданого значення n
    F = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        F[i][1] = 1
        F[i][i] = 1

    for i in range(3, n + 1):
        for j in range(2, i):
            F[i][j] = F[i - 1][j - 1] + j * F[i - 1][j]

    return F
def compute_bell(n): #використовує вже обчислені числа Стірлінга другого роду для обчислення чисел Белла.
    F = compute_stirling(n)
    B = [0] * (n + 1)

    for i in range(1, n + 1):
        B[i] = sum(F[i])

    return B
i = 1
n = i + 5
F = compute_stirling(n)
B = compute_bell(n)

print("Stirling numbers:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(F[i][j], end=" ")
    print()

print("Bell numbers:")
for i in range(1, n + 1):
    print(B[i], end=" ")
print()




