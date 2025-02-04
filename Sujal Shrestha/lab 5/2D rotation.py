import matplotlib.pyplot as plt
import numpy as np
x0 = int(input("Enter the point x0: "))
y0 = int(input("Enter the point y0: "))
x1 = int(input("Enter the point x1: "))
y1 = int(input("Enter the point y1: "))
theta = np.radians(int(input("enter rotation angle:")))
def Bresen(x0,y0,x1,y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1
#point initialization
    xes = [x0]
    yes = [y0]

    if dx > dy:
        p = 2 * dy - dx
        while x0 != x1:
            x0 = x0 + sx
            if p >= 0:
                y0 = y0 + sy
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            xes.append(x0)
            yes.append(y0)
    else:
        p = 2 * dx - dy
        while y0 != y1:
            y0 = y0 + sy
            if p >= 0:
                x0 = x0 + sx
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
            xes.append(x0)
            yes.append(y0)
    
    return xes,yes
xes,yes = Bresen(x0,y0,x1,y1)
T= np.array([[1,0,x1],[0,1,y1],[0,0,1]])
S= np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

NT= np.array([[1,0,-x1],[0,1,-y1],[0,0,1]])
CM= T@S@NT
print(CM)
points=np.vstack((xes,yes, np.ones_like(xes)))
TR= CM@points
 
plt.figure(figsize=(8,6))
plt.plot(xes, yes, marker='*',color='blue', linestyle='-', label='Original Line')

# Transformed line
plt.plot(TR[0],TR[1], color='red', linestyle='--', label='Transformed Line')

# Plot settings
plt.title("Bresenham Line with 2D Transformations")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()


