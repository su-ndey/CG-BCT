import matplotlib.pyplot as plt

x1=10
y1=15
x2=20
y2=30
 
del_x=x2-x1
del_y=y2-y1
 
steps=int(max(abs(del_x),abs(del_y)))

x_increment=del_x/steps
y_increment=del_y/steps

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
    
plt.plot(x_coordinate,y_coordinate)
plt.show()

