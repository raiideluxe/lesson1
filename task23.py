def my_filter(a):
    multiplied_nums = [str(num * 10) for num in a]
    return ' '.join(multiplied_nums)

numbers = [1, 2, 3, 4, 5]
result = my_filter(numbers)
print(result)
