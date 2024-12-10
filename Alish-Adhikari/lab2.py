#bresenham algorithm for all cases
import matplotlib.pyplot as plt
x1= int(input('Enter x1: '))
y1= int(input('Enter y1: '))
xo= int(input('Enter xo: '))
yo= int(input('Enter yo: '))

dx= abs(x1-xo)
dy= abs(y1-yo)
m=dy/dx


if x1>xo:
    sx=-1
else:
    sx=1

if y1>yo:
    sy=-1
else:
    sy=1

if abs(m)<=1:
    p=2*dy-dx
if abs(m)>1:
    p=2*dx-dy
k=0

xplot=[x1]
yplot=[y1]
for x1 in range(x1,xo):
     xplot.append(x1)
     yplot.append(y1)
     if abs(m)<=1:
        x1=x1+sx
        if p>=0:
            y1=y1+sy
            p= p+2*dy-2*dx
        else:
            p = p+2*dy
     if abs(m)>1:
        y1=y1+sy
        if p>=0:
            x1=x1+sx
            p=p+2*dx-2*dy
        else:
            p=p+2*dx
     print(f' {x1},{y1}   ')
plt.plot(xplot,yplot,marker='*')
plt.show()