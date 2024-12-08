import matplotlib.pyplot as pit

x1=int(input("Enter the starting x-coordinate"))
x2=int(input("Enter the ending x-coordinate"))
y1=int(input("Enter the sarting y coordinate"))
y2=int(input("Enter the ending y-coordinate"))

del_x=x2-x1
del_y=y2-y1

steps=int(max ( (del_x), (del_y) ))

x_increment=(del_x/steps)
y_increment=(del_y/steps)

x=x1
y=y1

x_coordinate=[x]
y_coordinate=[y]
for i in range(steps):
    x=x+x_increment
    x_coordinate.append(round(x))
    y=y+y_increment
    y_coordinate.append(round(y))

print(x_coordinate)
print(y_coordinate)
pit.plot(x_coordinate,y_coordinate)
pit.show()