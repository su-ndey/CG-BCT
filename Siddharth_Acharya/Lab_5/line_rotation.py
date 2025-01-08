import numpy as np
import matplotlib.pyplot as plt

# Bresenham Line Algorithm
def bresenham_line():
    # Taking Inputs from the user
    x1 = int(input("Enter x coordinate for the starting point: "))
    y1 = int(input("Enter y coordinate for the starting point: "))
    x2 = int(input("Enter x coordinate for the ending point: "))
    y2 = int(input("Enter y coordinate for the ending point: "))

    # Calculate differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine step directions
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    # Initialize decision parameters based on dominant axis
    points = []
    if dx >= dy:  # Shallow slope (|m| ≤ 1)
        p = 2 * dy - dx
        x, y = x1, y1
        for i in range(dx + 1):  # Include the endpoint
            points.append((x, y))
            x += sx
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
    else:  # Steep slope (|m| > 1)
        p = 2 * dx - dy
        x, y = x1, y1
        for i in range(dy + 1):  # Include the endpoint
            points.append((x, y))
            y += sy
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

    # Extract x and y coordinates for plotting
    x_list, y_list = zip(*points)
    return x_list, y_list, x1, y1


# Transformation Matrices
def translation_to_origin(tx, ty):
    return np.array([
        [1, 0, -tx],
        [0, 1, -ty],
        [0, 0, 1]
    ])

def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
        ])

def translation_back_from_origin(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])


# Get Bresenham line points
x_list, y_list, x1, y1 = bresenham_line()

# Transformation inputs
tx = x1
ty = y1
theta = np.pi / 4

# Composite transformation matrix
tto = translation_to_origin(tx, ty)
rm=rotation_matrix(theta)

tfo = translation_back_from_origin(tx, ty)

cm = tfo @ rm @ tto

# Apply transformation
points = np.vstack([x_list, y_list, np.ones_like(x_list)])
transformed_points = cm @ points
x_new, y_new = transformed_points[0], transformed_points[1]

# Plotting
plt.figure(figsize=(8, 6))

# Original line
plt.plot(x_list, y_list, marker='o', color='blue', label='Original Line')

# Transformed line
plt.plot(x_new, y_new, marker='x', color='red', linestyle='--', label='Transformed Line')

plt.title("Bresenham's Line with Scaling Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
