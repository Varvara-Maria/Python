import math

def calculate_sum(x, a, epsilon):
    k = 0
    result = 0
    while True:
        term = (math.sin(a**k) + math.cos(x**k)) / math.factorial(k**2)
        result += term
        k += 1
        if abs(term) < epsilon:
            break
    
    return result, k

x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))
epsilon = float(input("Введіть точність ε: "))

sum_result, num_terms = calculate_sum(x, a, epsilon)

print(f"Значення суми з точністю ε = {epsilon} дорівнює {sum_result}")
print(f"Кількість врахованих доданків: {num_terms}")
