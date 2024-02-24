room = int(input('Номер квартиры: '))
entrance = (room-1)//8+1
floor = (room-1)%8+1
print('Подъезд: ',entrance)
print('Этаж:',floor)

