import numpy as np
import matplotlib.pyplot as plt

# Input points
x0 = int(input("Enter the point x0: "))
y0 = int(input("Enter the point y0: "))
x1 = int(input("Enter the point x1: "))
y1 = int(input("Enter the point y1: "))
theta= np.radians(int(input('Enter angle to rotate: ')))

# Bresenham's Algorithm
def Bresen(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1
    xes, yes = [x0], [y0]
    
    if dx > dy:
        p = 2 * dy - dx
        while x0 != x1:
            x0 += sx
            if p >= 0:
                y0 += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            xes.append(x0)
            yes.append(y0)
    else:
        p = 2 *dx - dy
        while y0 != y1:
            y0 += sy
            if p >= 0:
                x0 += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            xes.append(x0)
            yes.append(y0)
    
    return xes, yes

# Generate line points
xes, yes = Bresen(x0, y0, x1, y1)

# Construct transformation matrices
T = np.array([[1, 0, x1], [0, 1, y1], [0, 0, 1]])
NT = np.array([[1, 0, -x1], [0, 1, -y1], [0, 0, 1]])
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]]) #rotation matrix

CM = T @ rotation_matrix @ NT  # Combined transformation matrix

# Apply transformation
points = np.vstack((xes, yes, np.ones_like(xes)))
TR = CM @ points
print(TR)

# Plot original and transformed lines
plt.figure(figsize=(8, 6))
plt.plot(xes, yes, marker='*', color='blue', linestyle='-', label='Original Line')
plt.plot(TR[0], TR[1], marker='o', color='red', linestyle='--', label='Transformed Line')
plt.title("Bresenham Line with 2D Transformations")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()