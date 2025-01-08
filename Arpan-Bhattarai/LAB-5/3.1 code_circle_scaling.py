import numpy as np
import matplotlib.pyplot as plt

# Function to calculate and collect symmetric points of the circle
def points_plot(xes, yes, x, y, xc, yc):
    xes.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

# Midpoint Circle Algorithm
def MidPointCircle():
    r = int(input("Enter the radius (r): "))
    xc = int(input("Enter the x-coordinate of the center (xc): "))
    yc = int(input("Enter the y-coordinate of the center (yc): "))

    x, y = 0, r
    p = 1 - r  # Decision parameter
    xes, yes = [], []

    # Add the initial points
    points_plot(xes, yes, x, y, xc, yc)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        points_plot(xes, yes, x, y, xc, yc)

    return np.array(xes), np.array(yes)

# Function to apply a 2D transformation
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])  # Convert to homogeneous coordinates
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

# Function to plot the original and transformed circle
def plot_circle_with_transformations():
    # Generate original circle points
    x_orig, y_orig = MidPointCircle()

    # Get the center of the circle
    xc, yc = x_orig[0], y_orig[0]

    # Scaling transformation matrix (scale x by 2, y by 0.5)
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 1]
    ])

    # Translation matrix to move the circle to the origin
    translation_to_origin = np.array([
        [1, 0, -xc],
        [0, 1, -yc],
        [0, 0, 1]
    ])

    # Translation matrix to move the circle back to its original center
    translation_back = np.array([
        [1, 0, xc],
        [0, 1, yc],
        [0, 0, 1]
    ])

    # Composite Transformation Matrix (Translation to Origin * Scaling * Translation Back)
    composite_matrix = translation_back @ scaling_matrix @ translation_to_origin

    # Apply the composite transformation
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Plot the original and transformed circles
    plt.figure(figsize=(8, 6))

    # Original circle
    plt.scatter(x_orig, y_orig, color='blue', s=10, label='Original Circle')

    # Transformed circle
    plt.scatter(x_transformed, y_transformed, color='red', s=10, label='Scaled Circle')

    # Plot settings
    plt.title("Midpoint Circle Algorithm with Center-Preserving Scaling")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Ensure equal aspect ratio for proper visualization
    plt.show()

# Call the function to execute the transformation and plot
plot_circle_with_transformations()
