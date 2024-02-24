def is_cell_black(pol):
    col = pol[0]
    row = int(pol[1])
    if (ord(col) - ord('a') + row) % 2 == 0:
        return True
    else:
        return False

pol = input('Координата строчной буквой: ')

if is_cell_black(pol):
    print('black')
else:
    print('white')
