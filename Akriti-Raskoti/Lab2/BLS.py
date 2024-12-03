import matplotlib.pyplot as plt
x1=int(input("Enter the starting x-coordinates:\n"))
y1=int(input("Enter the starting y-coordinates:\n"))
x2=int(input("Enter the edning x-coordinates:\n"))
y2=int(input("Enter the ending y-coordinates:\n"))

#the lists
xCord= []
yCord= []

#appending the lists
xCord.append(x1)
yCord.append(y1)

#delta
delta_x= x2-x1
delta_y= y2-y1

#decison paramater
p= 2* delta_y - delta_x

#loops to find other points
while x1<=x2:
    x1+=1
    if p<0:
        p= p+2*delta_y
    else:
        p= p+2*delta_y-2*delta_x
        y1+=1
    xCord.append(x1)
    yCord.append(y1)
    print(f"{x1},{y1}") 
plt.plot(xCord, yCord, marker="*")
plt.show()

