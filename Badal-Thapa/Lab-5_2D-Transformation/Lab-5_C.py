# Circle Transformation
import numpy as np
import matplotlib.pyplot as plt

def circle(radius, xc, yc):
    x, y = 0, radius
    p = 1 - radius
    x_es, y_es = [], []

    def plot_symmetric_points(x, y, xc, yc):
        # Append all symmetric points to the lists
        x_es.extend([x + xc, -x + xc, x + xc, -x + xc, y + xc, -y + xc, y + xc, -y + xc])
        y_es.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, -x + yc, -x + yc, x + yc])

    plot_symmetric_points(x, y, xc, yc)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_symmetric_points(x, y, xc, yc)

    return x_es, y_es

def apply_2d_transformation(x_es, y_es, transformation_matrix):
    points = np.vstack([x_es, y_es, np.ones_like(x_es)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_circle_with_transformations(radius, xc, yc, scale_factor=2):
    # Original circle points
    x_es, y_es = circle(radius, xc, yc)

    # Transformation matrices
    scaling_matrix = np.array([
        [scale_factor, 0, 0],
        [0, scale_factor, 0],
        [0, 0, 1]
    ])
    translation_matrix = np.array([
        [1, 0, xc],
        [0, 1, yc],
        [0, 0, 1]
    ])
    translation_inverse_matrix = np.array([
        [1, 0, -xc],
        [0, 1, -yc],
        [0, 0, 1]
    ])
    
    # Composite transformation
    composite_matrix = translation_matrix @ scaling_matrix @ translation_inverse_matrix
    x_transformed, y_transformed = apply_2d_transformation(x_es, y_es, composite_matrix)

    # Plotting
    plt.figure(figsize=(8, 8)) 
    plt.scatter(x_es, y_es, color='blue', label='Original Circle', s=10)
    plt.scatter(x_transformed, y_transformed, color='red', label='Transformed Circle', s=10)
    plt.title("Circle with 2D Transformations (Scaling and Translation)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal') 
    plt.legend()
    plt.grid(True)
    plt.show()
    
plot_circle_with_transformations(radius=100, xc=0, yc=0, scale_factor=2)
