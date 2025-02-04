import numpy as np
import matplotlib.pyplot as plt

# Input for line coordinates
x1 = int(input("Enter the starting x-coordinates:\n"))
y1 = int(input("Enter the starting y-coordinates:\n"))
x2 = int(input("Enter the ending x-coordinates:\n"))
y2 = int(input("Enter the ending y-coordinates:\n"))

# Bresenham's line algorithm to generate line points
def bresenham_line(x1, y1, x2, y2):
    xCord = []
    yCord = []
    
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    
    if x2 > x1:
        sx = 1
    else:
        sx = -1

    if y2 > y1:
        sy = 1
    else:
        sy = -1

    p = 2 * delta_y - delta_x if delta_x >= delta_y else 2 * delta_x - delta_y
    x, y = x1, y1
    xCord.append(x)
    yCord.append(y)
    
    if delta_x >= delta_y:
        while x != x2:
            x += sx
            if p < 0:
                p += 2 * delta_y
            else:
                p += 2 * (delta_y - delta_x)
                y += sy
            xCord.append(x)
            yCord.append(y)
    else:
        while y != y2:
            y += sy
            if p < 0:
                p += 2 * delta_x
            else:
                x += sx
                p += 2 * (delta_x - delta_y)
            xCord.append(x)
            yCord.append(y)
    
    return np.array(xCord), np.array(yCord)

# 2D Transformation function
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])  # Homogeneous coordinates
    transformed_points = transformation_matrix @ points  # Matrix multiplication
    return transformed_points[0], transformed_points[1]

# Function to apply Fixed Point Scaling and plot the result
def plot_line_with_fixed_point_scaling(x1, y1, x2, y2):
    # Generate original line points using Bresenham's algorithm
    x_orig, y_orig = bresenham_line(x1, y1, x2, y2)

    # Define the scaling matrix (scale x by 2, y by 0.5)
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ])
    
    # Define the fixed point (reference point for scaling)
    fixed_point = np.array([3, 3])

    # Translate points to the origin
    x_translated = x_orig - fixed_point[0]
    y_translated = y_orig - fixed_point[1]

    # Apply scaling
    scaled_x, scaled_y = apply_2d_transformation(x_translated, y_translated, scaling_matrix)

    # Translate points back to the original position
    x_scaled = scaled_x + fixed_point[0]
    y_scaled = scaled_y + fixed_point[1]

    # Plot original and transformed lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')

    # Transformed (scaled) line
    plt.plot(x_scaled, y_scaled, color='red', linestyle='--', label='Scaled Line')

    # Plot settings
    plt.title("Bresenham Line with Fixed Point Scaling")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

# Function to apply Rotation and plot the result
def plot_line_with_rotation(x1, y1, x2, y2):
    # Generate original line points using Bresenham's algorithm
    x_orig, y_orig = bresenham_line(x1, y1, x2, y2)

    # Rotation matrix for 45 degrees (theta = pi/4)
    theta = np.pi / 4
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Apply rotation through the origin
    x_rotated, y_rotated = apply_2d_transformation(x_orig, y_orig, rotation_matrix)

    # Plot original and rotated lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')

    # Rotated line
    plt.plot(x_rotated, y_rotated, color='green', linestyle='--', label='Rotated Line')

    # Plot settings
    plt.title("Bresenham Line with Rotation by 45 Degrees")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

# Call functions to plot the line with transformations
plot_line_with_fixed_point_scaling(x1, y1, x2, y2)  
plot_line_with_rotation(x1, y1, x2, y2)           
