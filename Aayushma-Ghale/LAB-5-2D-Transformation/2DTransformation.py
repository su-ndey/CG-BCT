import numpy as np  
import matplotlib.pyplot as plt

x1 = int(input('Enter the value of x1: '))
y1 = int(input('Enter the value of y1: '))
x2 = int(input('Enter the value of x2: '))
y2 = int(input('Enter the value of y2: '))

# Bresenham's Line Drawing Algorithm
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    xes = [x0]
    yes = [y0]
    p = 2 * dy - dx
    x = x0
    y = y0
    while x <= x1:
        if p < 0:
            xes.append(x)
            yes.append(y)
            x += 1
            p += 2 * dy
        else:
            xes.append(x)
            yes.append(y)
            x += 1
            y += 1
            p += 2 * dy - 2 * dx
    
    return xes, yes

# Apply 2D transformation (scaling + translation)
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    
    # Apply transformation matrix
    transformed_points = transformation_matrix @ points
    
    return transformed_points[0], transformed_points[1]

# Plotting original and transformed lines
def plot_line_with_transformation(x0, y0, x1, y1):
    # Generate original line points using Bresenham's algorithm
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Define transformation matrices
    # 1. Scaling Matrix (scale x by 4, y by 1.5)
    scaling_matrix = np.array([
        [4, 0, 0],
        [0, 1.5, 0],
        [0, 0, 1]
    ])
    
    # 2. Translation Matrix
    translation_matrix = np.array([
        [1, 0, x1],
        [0, 1, y1],
        [0, 0, 1]
    ])
    
    # 3. Inverse Translation Matrix
    inverse_translation_matrix = np.array([
        [1, 0, -x1],
        [0, 1, -y1],
        [0, 0, 1]
    ])

    # Composite Transformation Matrix
    composite_matrix = scaling_matrix @ translation_matrix @ inverse_translation_matrix
    
    # Apply transformation to the original points
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Create the plot
    plt.figure(figsize=(8, 6))
    
    # Plot original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    
    # Plot transformed line
    plt.plot(x_transformed, y_transformed, marker='o', color='red', linestyle='-', label='Transformed Line')
    
    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    
    plt.show()

# Call the function to plot the line with transformation
plot_line_with_transformation(2, 3, 10, 8)
