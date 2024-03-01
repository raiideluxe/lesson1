def trapez(func, a, b, N):
    h = (b - a) / N
    integral = (func(a) + func(b)) / 2
    for i in range(1, N):
        integral += func(a + i * h)
    integral *= h

    return round(integral, 8)

# Пример использования функции
import math

def my_func(x):
    return math.sin(x)

a = 0
b = 5
N = 1000

result = trapez(my_func, a, b, N)
print(result)