def ak(k):
    if k == 1:
        return 1
    else:
        return 3 * bk(k - 1) + 2 * ak(k - 1)

def bk(k):
    if k == 1:
        return 1
    else:
        return ak(k - 1) ** 2 + bk(k - 1)

def calculate_sum(n, a, b, k=1):
    if k > n:
        return 0
    else:
        term = 2**k / (1 + a(k) + b(k))
        return term + calculate_sum(n, a, b, k + 1)

n = int(input("Введіть значення n: "))
result = calculate_sum(n, ak, bk)
print(f"Результат обчислення суми для n={n}: {result}")