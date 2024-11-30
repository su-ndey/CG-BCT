import matplotlib.pyplot as plt
x1=10
y1=15
x2=20
y2=30
dx=abs(x2-x1)
dy=abs(y2-y1)
steps=int(max(dx,dy))
x_incr=(dx/steps)
y_incr=(dy/steps)
x=x1
y=y1
x_list=[]
y_list=[]
for i in range (steps):
    x_list.append(round(x+x_incr))
    x=x+x_incr
    y_list.append(round(y+y_incr))
    y=y+y_incr
print(x_list)
print(y_list)
print(f"The Starting Point is {x},{y}")
plt.figure(figsize=(7, 7))
plt.plot(x_list, y_list)
plt.show()