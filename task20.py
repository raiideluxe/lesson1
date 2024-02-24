def teylor_logarithm(x):
    result = 0
    term = x
    term_number = 2

    while abs(term) > 1e-6:
        result += term
        term *= -x * (term_number-1)/term_number
        term_number+=1

    return round(x,8)

x = input()

result = teylor_logarithm(x)
print(result)