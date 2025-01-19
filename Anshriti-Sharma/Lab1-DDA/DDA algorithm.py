#DDA algorithm
import matplotlib.pyplot as plt
x1= int(input('Enter x1: '))
y1= int(input('Enter y1: '))
x2= int(input('Enter x2: '))
y2= int(input('Enter y2: '))
dx= x2-x1
dy= y2-y1
print(dx)
print(dy)
steps= max(abs(dx),abs(dy))
xincrement=dx/steps
yincrement=dy/steps
x=x1
y=y1
xplot=[x1]
yplot=[y1]
for i in range (steps):
    x=x+xincrement
    y=y+yincrement
    xplot.append(x)
    yplot.append(y)
    print(f' {x},{y}   ')
plt.plot(xplot,yplot,marker='*')
plt.show()