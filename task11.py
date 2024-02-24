melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455,'Si': 1415, 'Be': 1287}
element1 = input('first element:')
element2 = input('second element:')
if element1 in melt and element2 in melt:
    difference = abs(melt[element1]-melt[element2])
    print(difference)
else:
    print('incorrect name of element!')