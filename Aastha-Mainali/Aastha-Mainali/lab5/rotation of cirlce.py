#rotation of circle by 45 degree
import numpy as np
import matplotlib.pyplot as plt

# Function to apply 2D transformations
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])

    # Apply transformation matrix (matrix multiplication)
    transformed_points = transformation_matrix @ points

    return transformed_points[0], transformed_points[1]

# Function to plot circle with transformations
def plot_circle_with_transformations(center, radius, rotation_angle):
    # Generate original circle points using parametric equation
    theta = np.linspace(0, 2 * np.pi, 100)
    x_orig = center[0] + radius * np.cos(theta)
    y_orig = center[1] + radius * np.sin(theta)

    # Rotation Matrix (rotate by `rotation_angle` degrees)
    rotation_matrix = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle), 0],
        [np.sin(rotation_angle), np.cos(rotation_angle), 0],
        [0, 0, 1]
    ])

    # Apply transformation (rotation)
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, rotation_matrix)

    # Plotting the original and transformed circles
    plt.figure(figsize=(8, 8))

    # Plot the original circle (in blue)
    plt.plot(x_orig, y_orig, color='blue',marker='*', linestyle='-', label='Original Circle')

    # Plot the transformed circle (in red)
    plt.plot(x_transformed, y_transformed, color='red',marker='*',  linestyle='--', label='Rotated Circle')

    # Plot settings
    plt.title(f"Circle Rotation by 45 Degrees")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')

    plt.show()

# Example Usage: Plot the circle with center (0, 0) and radius 5, and rotate by 45 degrees
plot_circle_with_transformations(center=(0, 0), radius=5, rotation_angle=np.pi / 4)