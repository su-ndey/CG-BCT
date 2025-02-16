import numpy as np
import matplotlib.pyplot as plt
def Circle(xc,yc,r):
    

    # Lists to store circle points
    xes = []
    yes = []

    # Function to plot symmetric points
    def SymmetryPlotter(xes, yes, x, y, xc, yc):
        xes.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, -y + xc, y + xc])
        yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

    # Initial conditions
    x = 0
    y = r
    p = 1 - r

    # Plot initial points
    SymmetryPlotter(xes, yes, x, y, xc, yc)

    # Midpoint Circle Algorithm
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        SymmetryPlotter(xes, yes, x, y, xc, yc)

    return xes,yes

xc=int(input("enter xc: "))
yc=int(input("enter yc: "))
r=int(input("enter r: "))

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]



def plot_line_with_scaling(xc, yc,r):
    sx=2
    sy=2
    x_orig, y_orig = Circle(xc,yc,r)
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    

    translation_matrix = np.array([
        [1, 0, xc],
        [0, 1, yc],
        [0, 0, 1]
    ])
    translation_matrix_dash = np.array([
        [1, 0, -xc],
        [0, 1, -yc],
        [0, 0, 1]
    ])
    composite_matrix=translation_matrix @ scaling_matrix @ translation_matrix_dash
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)
      # Plot original and transformed lines
    plt.figure(figsize=(8, 8))


    # Original line


    plt.scatter(x_orig, y_orig, marker='*',color='blue', linestyle='-', label='Original Line')


    # Transformed line
    plt.scatter(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')


    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


    plt.show()

def plot_line_with_rotation(xc,yc,r):
    
    x_orig, y_orig = Circle(xc,yc,r)
    
    theta = np.pi / 4  # 45 degrees
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


    translation_matrix = np.array([
        [1, 0, xc],
        [0, 1, yc],
        [0, 0, 1]
    ])
    translation_matrix_dash = np.array([
        [1, 0, -xc],
        [0, 1, -yc],
        [0, 0, 1]
    ])
    composite_matrix=translation_matrix @ rotation_matrix @ translation_matrix_dash
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)
      # Plot original and transformed lines
    plt.figure(figsize=(8, 6))


    # Original line


    plt.scatter(x_orig, y_orig, marker='*',color='blue', linestyle='-', label='Original Line')


    # Transformed line
    plt.scatter(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')


    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


    plt.show()

plot_line_with_scaling(1,2,6)