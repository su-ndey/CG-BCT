import matplotlib.pyplot as plt
import numpy as np

# Input the center and radius of the circle
xc = int(input("Enter the center xc: "))
yc = int(input("Enter the center yc: "))
r = int(input("Enter the radius r: "))

def circle(xc, yc, r):
    p = 1 - r
    xe, ye = [], []
    x = 0
    y = r

    def symmetry(xe, ye, x, y, xc, yc):
        """Add symmetry points of the circle"""
        xe.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, y + xc, -y + xc])
        ye.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

    symmetry(xe, ye, x, y, xc, yc)
    
    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        symmetry(xe, ye, x, y, xc, yc)

    return xe, ye

# Generate circle points
xe, ye = circle(xc, yc, r)

# Input scaling factors
sx = int(input("Enter scaling factor sx: "))
sy = int(input("Enter scaling factor sy: "))

# Construct scaling transformation matrix
S = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

# Prepare points for transformation
points = np.vstack((xe, ye, np.ones_like(xe)))

# Apply scaling transformation
transformed_points = S @ points
transformed_xe, transformed_ye = transformed_points[0], transformed_points[1]

# Plot original and transformed circles
plt.figure(figsize=(8, 8))
plt.scatter(xe, ye, color='blue', label='Original Circle', s=10)
plt.scatter(transformed_xe, transformed_ye, color='red', label='Scaled Circle', s=10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Circle Drawing with Scaling Transformation")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()