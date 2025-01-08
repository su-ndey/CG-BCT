import matplotlib.pyplot as plt
import numpy as np

# Function to calculate and plot the symmetric points of the circle
def points_plot(xes, yes, x, y, xc, yc): 
    # Extend the x and y lists with 8 symmetric points for the current (x, y)
    xes.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

# Main function to implement the Midpoint Circle Algorithm
def MidPointCircle():
    # Taking radius and center coordinates as input from the user
    r = int(input("Enter the radius (r): "))
    xc = int(input("Enter the x-coordinate of the center (xc): "))       
    yc = int(input("Enter the y-coordinate of the center (yc): "))
   
    # Initializing variables
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter
    
    # Lists to store circle points
    xes = []
    yes = []
    
    # Plot the initial points
    points_plot(xes, yes, x, y, xc, yc)
    
    # Iterate while x is less than y
    while x < y:
        x = x + 1  # Increment x
        if p < 0:
            # If decision parameter is negative, update it for the next step
            p = p + 2 * x + 1
        else:
            # If decision parameter is non-negative, update y and the parameter
            y = y - 1
            p = p + 2 * (x - y) + 1 

        # Call function to add new points
        points_plot(xes, yes, x, y, xc, yc)

    return np.array(xes), np.array(yes), xc, yc

# Function to apply 2D transformation
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

# Function to rotate the circle points
def plot_circle_with_rotation():
    # Generate the circle points using Midpoint Circle Algorithm
    x_orig, y_orig, xc, yc = MidPointCircle()

    # Define the rotation matrix (rotate 45 degrees around the center of the circle)
    theta = np.pi / 2  # 45 degrees
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Define the translation matrices to rotate around the circle's center
    translation_matrix = np.array([
        [1, 0, xc],
        [0, 1, yc],
        [0, 0, 1]
    ])
    reverse_translation_matrix = np.array([
        [1, 0, -xc],
        [0, 1, -yc],
        [0, 0, 1]
    ])

    # Composite Transformation Matrix (Translation * Rotation * Reverse Translation)
    composite_matrix = translation_matrix @ rotation_matrix @ reverse_translation_matrix

    # Apply the transformation
    x_rotated, y_rotated = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Plot the original and rotated circles
    plt.figure(figsize=(8, 6))

    # Original circle
    plt.plot(x_orig, y_orig, marker='o', color='blue', linestyle='', label='Original Circle')

    # Rotated circle
    plt.plot(x_rotated, y_rotated, marker='o', color='red', linestyle='', label='Rotated Circle')

    # Plot settings
    plt.title("Midpoint Circle Algorithm with Rotation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Ensure equal scaling
    plt.show()

# Call the function to execute
plot_circle_with_rotation()
