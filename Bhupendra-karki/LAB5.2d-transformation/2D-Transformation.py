#2d-transformation
import numpy as np
import matplotlib.pyplot as plt

def BLA():
    x1 = int(input('Enter the starting x-coordinate: '))
    y1 = int(input('Enter the starting y-coordinate: '))
    x2 = int(input('Enter the ending x-coordinate: '))
    y2 = int(input('Enter the ending y-coordinate: '))

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x = 1 if x2 > x1 else -1
    y = 1 if y2 > y1 else -1

    x_plot = [x1]
    y_plot = [y1]

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            x1 += x
            if p >= 0:
                y1 += y
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
            x_plot.append(x1)
            y_plot.append(y1)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            y1 += y
            if p >= 0:
                x1 += x
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx
            x_plot.append(x1)
            y_plot.append(y1)

    return x_plot, y_plot

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations():
    x_orig, y_orig = BLA()

    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ])
    translation_matrix = np.array([
        [1, 0, 3],
        [0, 1, 2],
        [0, 0, 1]
    ])
    inverse_translation_matrix = np.array([
        [1, 0, -3],
        [0, 1, -2],
        [0, 0, 1]
    ])

    composite_matrix = inverse_translation_matrix @ scaling_matrix @ translation_matrix
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, marker='o', color='red', linestyle='--', label='Transformed Line')
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
plot_line_with_transformations()

         
         








