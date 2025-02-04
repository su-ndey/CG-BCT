import numpy as np
import matplotlib.pyplot as plt
def circle(r, xc, yc):
    x =0
    y =r
    p =1-r
    xes =[]
    yes =[]
    def plot(x,y,xc,yc):
        xes.extend([x+ xc, -x+ xc, x+ xc, -x+ xc, y+ xc, -y+ xc, y+ xc, -y+ xc])
        yes.extend([y+ yc, y+ yc, -y+ yc, -y+ yc, x+ yc, -x+ yc, -x+ yc, x+ yc])
    plot(x,y,xc,yc)
    while x<y:
        x+=1
        if p<0:
            p =p+2*x+1
        else:
            y-=1
            p = p+2*(x-y)+1
        plot(x,y,xc,yc)
    return xes, yes

def apply_2d_transformation(xes, yes, transformation_matrix):
    points = np.vstack([xes, yes, np.ones_like(xes)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations(r, xc, yc):
    xes, yes = circle(r, xc, yc)
    scaling_matrix = np.array([[2, 0, 0],[0, 2, 0],[0, 0, 1]])
    translation_matrix = np.array([[1, 0, 2],[0, 1, 3],[0, 0, 1]])
    translation = np.array([[1, 0, -2],[0, 1, -3],[0, 0, 1]])

    composite_matrix =translation_matrix @ scaling_matrix @ translation
    
    x_transformed, y_transformed = apply_2d_transformation(xes, yes, composite_matrix)

    plt.figure(figsize=(8, 6))
    plt.scatter(xes, yes, marker='*', color='blue')
    plt.scatter(x_transformed, y_transformed, color='red')

    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_line_with_transformations(50, 2, 3)