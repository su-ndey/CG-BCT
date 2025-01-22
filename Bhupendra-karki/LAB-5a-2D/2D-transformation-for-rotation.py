import numpy as np
import matplotlib.pyplot as plt

def bresenham_line():
    # Input the points
    x0 = int(input("Enter the point x0: "))
    y0 = int(input("Enter the point y0: "))
    x1 = int(input("Enter the point x1: "))
    y1 = int(input("Enter the point y1: "))

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

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

    return np.array(xes), np.array(yes)

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])

    # Apply transformation matrix
    transformed_points = transformation_matrix @ points

    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations():
    # Generate original line points using Bresenham's Line Algorithm
    x_orig, y_orig = bresenham_line()

    # Define the rotation matrix to rotate by 45 degrees around the origin
    theta = np.pi / 4  # 45 degrees
    rotation_matrix = np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Use x0 and y0 from the input points as translation vector
    x0, y0 = x_orig[0], y_orig[0]  # Get the starting point coordinates

    # Define the translation matrix to move the line by x0 units right and y0 units up
    translation_matrix = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])

    # Define the reverse translation matrix to move the line back by x0 and y0 units
    translationve_matrix = np.array([
        [1, 0, -x0],
        [0, 1, -y0],
        [0, 0, 1]
    ])

    # Composite Transformation Matrix (Translation * Rotation * Reverse Translation)
    composite_matrix = translation_matrix @ rotation_matrix @ translationve_matrix

    # Apply the composite transformation to the original line
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Plot the original and transformed lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')

    # Transformed line
    plt.plot(x_transformed, y_transformed, marker='o',color='red', linestyle='--', label='Transformed Line')

    # Plot settings
    plt.title("Bresenham Line with 2D Transformations (Rotation and Translation)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

# Example Usage
plot_line_with_transformations()

