def write(filename, data):
    with open(filename, 'w') as file:
        for measure in data:
            time, value = measure
            file.write(f"{time}\t{value}\n")

filename = "1.txt"
data = [(1, 20), (2, 30), (3, 40), (4, 35), (5, 22), (6, 10)]
write(filename, data)
