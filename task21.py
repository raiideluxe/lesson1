import numpy as np
x = [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]
speed = np.diff(x) / 0.01
max_speed = np.max(np.abs(speed))
print(f"Максимальный модуль скорости частицы: {max_speed} нм/с")