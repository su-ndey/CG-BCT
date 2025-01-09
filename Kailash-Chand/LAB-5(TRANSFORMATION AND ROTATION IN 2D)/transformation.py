import numpy as np
import matplotlib.pyplot as plt

def BLA(x0,y0, x1, y1):

    delx = abs(x1 - x0)
    dely = abs(y1 - y0)
    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1
    xes = [x0]
    yes = [y0]
    
    if delx > dely : 
        p = 2*dely - delx
        for i in range(max(x1, x0)-1):
            x0 = x0 + sx
            if p >= 0:
                y0 = y0 + sy
                p = p + 2*dely -2*delx
            else:
                p = p + 2*dely
            xes.append(x1)
            yes.append(y1)
            
    else: 
        p = 2*delx - dely
        for i in range(max(x1, x0)-1):
            y0 = y0 + sy
            if p >= 0:
                x0 = x0 + sx
                p = p + 2*delx -2*dely
            else:
                p = p + 2*delx
            xes.append(x1)
            yes.append(y1)
    return xes, yes

def apply_2d_transformation(xes, yes, transformation_matrix):
    points = np.vstack([xes, yes, np.ones_like(xes)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations(x0, y0, x1, y1):
    xes, yes = BLA(x0, y0, x1, y1)
    scaling_matrix = np.array([[2, 0, 0],[0, 0.5, 0],[0, 0, 1]])
    translation_matrix = np.array([[1, 0, x0],[0, 1, y0],[0, 0, 1]])
    translation = np.array([[1, 0, -x0],[0, 1, -y0],[0, 0, 1]])

    composite_matrix =translation_matrix @ scaling_matrix @ translation
    
    x_transformed, y_transformed = apply_2d_transformation(xes, yes, composite_matrix)

    plt.figure(figsize=(8, 6))
    plt.plot(xes, yes, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')

    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_line_with_transformations(2, 3, 10, 8)
