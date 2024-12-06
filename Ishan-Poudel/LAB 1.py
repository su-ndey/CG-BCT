import matplotlib.pyplot as plt
xcoord= []
ycoord=[]
x1= int(input("Enter the x1-coordinate: \n"))
xcoord.append(x1)
y1= int(input("Enter the y1-coordinate: \n"))
ycoord.append(y1)
x2= int(input("Enter the x2-coordinate: \n"))
# coord.append(x2)
y2= int(input("Enter the y2-coordinate: \n"))
# coord.append(y2)

# print(coord)

delta_x= x2-x1
delta_y= y2- y1

steps=max(delta_x,delta_y)

x_inc= delta_x/steps
y_inc= delta_y/steps

for i in range(steps):
    x1=x1+x_inc
    y1=y1+y_inc
    xcoord.append(x1)
    ycoord.append(y1)
    print({x1},{y1} ) 

plt.plot(xcoord, ycoord, marker='o')
plt.show()
