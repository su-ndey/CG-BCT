import numpy as np
import matplotlib.pyplot  as plt

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

def apply_2d_rotation(xes, yes, rotation_matrix):
    points = np.vstack([xes, yes, np.ones_like(xes)])
    rotated_points = rotation_matrix @ points
    return rotated_points[0], rotated_points[1]

def plot_line_with_rotations(r, xc, yc):
    xes, yes = circle(r, xc, yc)
    theta = np.pi / 4 
    translation_matrix = np.array([[1, 0, xc],[0, 1, yc],[0, 0, 1]])
    translation = np.array([[1, 0, -xc],[0, 1, -yc],[0, 0, 1]])    
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0],[0, 0, 1]])
    composite_matrix = translation_matrix @ rotation_matrix @ translation
    x_rotated, y_rotated = apply_2d_rotation(xes, yes, composite_matrix)
    plt.figure(figsize=(8, 6))
    plt.scatter(xes, yes, color='blue')
    plt.scatter(x_rotated, y_rotated, color='red')

    plt.title("Circle with 2D Rotation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()   

plot_line_with_rotations(100, 2, 3)