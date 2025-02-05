import numpy as np
import matplotlib.pyplot as plt

def BLA(x0,y0,x1,y1):

    del_x=abs(x1-x0)
    del_y=abs(y1-y0)

    sx=1 if x1>x0 else -1
    sy=1 if y1>y0 else -1

    if del_x>=del_y: ##For shallow slopes
        pk=2*del_y-del_x
    else: ##for steep slope
        pk=2*del_x-del_y


    xes=[x0]
    yes=[y0]
    x=x0
    y=y0
    for k in range (max(del_x,del_y)):
        if del_x>=del_y: ##for shallow slope

            x+=sx
            if pk>=0:
                y+=sy
                pk=pk+2*del_y-2*del_x
            
            else:
                pk=pk+2*del_y
            xes.append(x)
            yes.append(y)  
        else:
            y+=sy
            if pk>=0:
                x+=sx
                pk=pk+2*del_x-2*del_y

            else:
                pk=pk+2*del_x
            xes.append(x)
            yes.append(y)  
    return xes,yes






def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]



def plot_line_with_scaling(x0, y0, x1, y1):
    sx=2
    sy=0.5
    x_orig, y_orig = BLA(x0, y0, x1, y1)
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])
    

    translation_matrix = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])
    translation_matrix_dash = np.array([
        [1, 0, -x0],
        [0, 1, -y0],
        [0, 0, 1]
    ])
    composite_matrix=translation_matrix @ scaling_matrix @ translation_matrix_dash
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)
      # Plot original and transformed lines
    plt.figure(figsize=(8, 6))


    # Original line


    plt.plot(x_orig, y_orig, marker='*',color='blue', linestyle='-', label='Original Line')


    # Transformed line
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')


    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


    plt.show()

def plot_line_with_rotation(x0, y0, x1, y1):
    
    x_orig, y_orig = BLA(x0, y0, x1, y1)
    
    theta = np.pi / 4  # 45 degrees
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


    translation_matrix = np.array([
        [1, 0, x0],
        [0, 1, y0],
        [0, 0, 1]
    ])
    translation_matrix_dash = np.array([
        [1, 0, -x0],
        [0, 1, -y0],
        [0, 0, 1]
    ])
    composite_matrix=translation_matrix @ rotation_matrix @ translation_matrix_dash
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)
      # Plot original and transformed lines
    plt.figure(figsize=(8, 6))


    # Original line


    plt.plot(x_orig, y_orig, marker='*',color='blue', linestyle='-', label='Original Line')


    # Transformed line
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')


    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)


    plt.show()

plot_line_with_rotation(1,2,6,9)