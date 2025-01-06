import numpy as np
import matplotlib.pyplot as plt

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
tx = int(input('Enter tx: '))
ty = int(input('Enter ty: '))
sx = float(input('Enter scaling factor sx: '))
sy = float(input('Enter scaling factor sy: '))
theta = np.radians(float(input('enter angle:')))

def bresenham(x1, y1, x2, y2):
 
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx_step = 1 if x1 < x2 else -1
    sy_step = 1 if y1 < y2 else -1

    xes = [x1]
    yes = [y1]

    if dx > dy: 
        p = 2 * dy - dx
        while x1 != x2:
            x1 += sx_step
            if p >= 0:
                y1 += sy_step
                p -= 2 * dx
            p += 2 * dy
            xes.append(x1)
            yes.append(y1)
    else:  
        p = 2 * dx - dy
        while y1 != y2:
            y1 += sy_step
            if p >= 0:
                x1 += sx_step
                p -= 2 * dy
            p += 2 * dx
            xes.append(x1)
            yes.append(y1)
    
    return xes, yes

xes, yes = bresenham(x1, y1, x2, y2)


t = np.array([[1, 0, -x1], [0, 1, -y1], [0, 0, 1]])  # Translation matrix
s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])  # Scaling matrix
rm= np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]])
tr = np.array([[1, 0, x1], [0, 1, y1], [0, 0, 1]])  # Reverse translation matrix
cm = tr @ rm @ s @ t  # Combined transformation matrix


# Apply transformation
ts = np.vstack((xes, yes, np.ones_like(xes)))  
nc = cm @ ts  # Transformed coordinates

plt.figure(figsize=(8, 6))

# Original line
plt.plot(xes, yes, marker='o', color='blue', linestyle='-', label='Original Line')

# Transformed line
plt.plot(nc[0], nc[1], color='red', linestyle='--', label='Transformed Line')

plt.title("Bresenham Line with 2D Transformations")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

plt.show()