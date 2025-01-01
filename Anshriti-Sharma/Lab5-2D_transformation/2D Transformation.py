import numpy as np
import matplotlib.pyplot as plt
x1= int(input('Enter x1: '))
y1= int(input('Enter y1: '))
xo= int(input('Enter xo: '))
yo= int(input('Enter yo: '))
tx= int(input('Enter tx: '))
ty= int(input('Enter ty: '))
sx= int(input('Enter sx: '))
sy= int(input('Enter sy: '))
theta= np.radians(int(input('Enter angle to rotate: ')))
def bresenham(x1,y1,xo,yo):
   
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

    xes=[x1]
    yes=[y1]
    for x1 in range(x1,xo):
        xes.append(x1)
        yes.append(y1)
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
    return xes,yes

xes,yes= bresenham(x1,y1,xo,yo)

t = np.array([[1,0,-x1],[0,1,-y1],[0,0,1]]) #translation matrix
s = np.array([[sx,0,0],[0,sy,0],[0,0,1]]) #scaling matrix
T = np.array([[1,0,x1],[0,1,y1],[0,0,1]]) #inverse translation matrix
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]]) #rotation matrix

CM = t @ rotation_matrix @ s @ T #composite matrix
points = np.vstack((xes,yes,np.ones_like(xes))) #stacked points

TR = CM @ points #transformed matrix
plt.figure(figsize=(8, 6))
plt.plot(xes,yes ,marker='*',color='blue', linestyle='-', label='Original Line')
plt.plot(TR[0],TR[1], color='red', linestyle='--', label='Transformed Line')

plt.title("Bresenham Line with 2D Transformations")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
