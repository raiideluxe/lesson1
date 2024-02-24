def is_point_in_circle(x,y):
    return (x-1)**2 + y**2 <= 2**2 and (x-1)**2 + y**2>=1**2
def is_point_in_rectangle(x,y):
    return abs(x-4)<2 and abs(y-2)<3
x = int(input('x:'))
y = int(input('y:'))
if is_point_in_circle(x,y) and is_point_in_rectangle(x,y):
    print('yes yes')
if is_point_in_circle(x,y):
    print('yes no')
if is_point_in_rectangle(x,y):
    print('no yes')
else:
    print('no no')
