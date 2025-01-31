#fixed point scaling of a line
import numpy as np
import matplotlib.pyplot as plt

# Bresenham Line Function (Assumed to be provided)
def bresenham_line(x0, y0, x1, y1):
    xes, yes = [], []
    # Implement Bresenham's line algorithm
    # For simplicity, using a placeholder line between (x0, y0) and (x1, y1)
    steps = max(abs(x1 - x0), abs(y1 - y0))
    for i in range(steps + 1):
        x = x0 + i * (x1 - x0) // steps
        y = y0 + i * (y1 - y0) // steps
        xes.append(x)
        yes.append(y)
    return xes, yes

# Function to apply 2D transformations
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
                         #vstack to create vertical array of x,y,1
    # Apply transformation matrix
    transformed_points = transformation_matrix @ points

    return transformed_points[0], transformed_points[1]

# Function to plot line with transformations
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

    # Fixed-point scaling factor (e.g., scaling by 2^8)
    S = 2**8  # Scaling factor (256)

    # Fixed-point scaling matrix
    fixed_point_scaling_matrix = np.array([
        [S, 0, 0],
        [0, S, 0],
        [0, 0, 1]
    ])

    # Combine scaling, translation, and fixed-point scaling matrices
    composite_matrix = translation_matrix @ scaling_matrix @ fixed_point_scaling_matrix

    # Apply transformations
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Convert back from fixed-point (divide by S)
    x_transformed_float = x_transformed / S
    y_transformed_float = y_transformed / S

    # Plot original and transformed lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='green', linestyle='-', label='Original Line')

    # Transformed line
    plt.plot(x_transformed_float, y_transformed_float, color='red', linestyle='--', label='Transformed Line')

    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)

    plt.show()

# Example Usage
plot_line_with_transformations(2, 3, 10, 8)