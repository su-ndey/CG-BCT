import numpy as np
import matplotlib.pyplot as plt

# Circle Algorithm
def circle():
    # Take inputs for the center point and radius
    xc = int(input("Enter x-coordinate for the center point: "))
    yc = int(input("Enter y-coordinate for the center point: "))
    r = int(input("Enter the radius: "))

    # Initialize lists for circle points
    xes, yes = [], []

    # Initialize variables
    x, y = 0, r
    p = 1 - r

    # Function to add symmetric points
    def add_circle_points(xc, yc, x, y):
        xes.extend([xc + x, xc - x, xc + y, xc - y, xc + x, xc - x, xc + y, xc - y])
        yes.extend([yc + y, yc + y, yc + x, yc + x, yc - y, yc - y, yc - x, yc - x])

    # Add initial points
    add_circle_points(xc, yc, x, y)

    # Midpoint Circle Algorithm
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        add_circle_points(xc, yc, x, y)

    # Zip the points into x_list and y_list
    x_list, y_list = zip(*sorted(zip(xes, yes)))
    return x_list, y_list, xc, yc


# Transformation Matrices
def translation_to_origin(tx, ty):
    return np.array([
        [1, 0, -tx],
        [0, 1, -ty],
        [0, 0, 1]
    ])

# def scaling_matrix(sx, sy):
#     return np.array([
#         [sx, 0, 0],
#         [0, sy, 0],
#         [0, 0, 1]
#     ])

def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
        ])

def translation_back_from_origin(tx,ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])


# Get Circle points
x_list, y_list, xc, yc = circle()

# Transformation inputs
tx = xc
ty = yc
# sx = 2
# sy = 0.5
theta = np.pi / 4

# Composite transformation matrix
tto = translation_to_origin(tx, ty)
rm=rotation_matrix(theta)
# sm = scaling_matrix(sx, sy)
tfo = translation_back_from_origin(tx, ty)
# cm = tfo @ sm @ tto
cm = tfo @ rm @ tto

# Apply transformation
points = np.vstack([x_list, y_list, np.ones_like(x_list)])
transformed_points = cm @ points
x_new, y_new = transformed_points[0], transformed_points[1]

# Plotting
plt.figure(figsize=(6, 6))

# Original line
plt.scatter(x_list, y_list, marker='o', color='blue', label='Original Circle')

# Transformed line
plt.scatter(x_new, y_new, marker='x', color='red', linestyle='--', label='Transformed Circle')

plt.title("Circle with Scaling Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
