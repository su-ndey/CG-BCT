import numpy as np
import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    # Bresenham's Line Drawing Algorithm
    x, y = x0, y0
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    xes, yes = [], []

    while True:
        xes.append(x)
        yes.append(y)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return xes, yes

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    
    # Apply transformation matrix
    transformed_points = transformation_matrix @ points
    
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations(x0, y0, x1, y1):
    # Generate original line points
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Define transformation matrices
    # 1. Scaling Matrix (scale x by 2, y by 0.5)
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ])

    # 2. Translation Matrix (translate by 3 units right and 2 units up)
    translation_matrix = np.array([
        [1, 0, 3],
        [0, 1, 2],
        [0, 0, 1]
    ])

    # 3. Fixed Point Scaling Matrix (scale x by 2, y by 0.5 around fixed point (0, 0))
    xc, yc = 0, 0  # Fixed point (can be any point, here we choose (0,0))
    s_x, s_y = 2, 0.5  # Scaling factors

    fixed_point_scaling_matrix = np.array([
        [s_x, 0, (1 - s_x) * xc],
        [0, s_y, (1 - s_y) * yc],
        [0, 0, 1]
    ])

    # 4. Rotation Matrix (rotate by 45 degrees)
    theta = np.pi / 4  # 45 degrees
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Apply transformations
    x_scaled, y_scaled = apply_2d_transformation(x_orig, y_orig, scaling_matrix)
    x_rotated, y_rotated = apply_2d_transformation(x_orig, y_orig, rotation_matrix)
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, translation_matrix @ fixed_point_scaling_matrix @ rotation_matrix)

    # Plot original, scaled, rotated, and transformed lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='o', color='blue', linestyle='-', label='Original Line')

    # Scaled line
    plt.plot(x_scaled, y_scaled, marker='x', color='green', linestyle='-', label='Scaled Line')

    # Rotated line
    plt.plot(x_rotated, y_rotated, marker='s', color='purple', linestyle='-', label='Rotated Line')

    # Transformed line
    plt.plot(x_transformed, y_transformed, marker='o', color='red', linestyle='--', label='Transformed Line')

    # Plot settings
    plt.title("Bresenham Line with 2D Transformations (Scaling, Translation, Rotation)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

# Test with some example points
plot_line_with_transformations(2, 3, 10, 8)



