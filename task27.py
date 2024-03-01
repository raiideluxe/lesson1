def volume(a, b, c=None):
    if c is None:
        # Вычисляем площадь прямоугольника
        return a * b
    else:
        # Вычисляем объем параллелепипеда
        return a * b * c

# Примеры использования функции
area = volume(2, 3)
print("Площадь прямоугольника:", area)

volume = volume(2, 3, 4)
print("Объем параллелепипеда:", volume)