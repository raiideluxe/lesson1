def ln_1_plus_x(x):
    result = 0
    term = x
    n = 1

    while abs(term) >= 10**-6:
        result += term
        n += 1
        term = (-1)**(n-1) * x**n / n

    return round(result, 8)

x = 0.5
result = ln_1_plus_x(x)
print(result)