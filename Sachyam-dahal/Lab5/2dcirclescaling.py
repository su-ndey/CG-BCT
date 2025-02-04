import matplotlib.pyplot as plt
import numpy as np
def plot_circle_points(x_center, y_center, x, y, points):
   
    
    
    points.append((x_center + x, y_center + y))  
    points.append((x_center - x, y_center + y)) 
    points.append((x_center + x, y_center - y))  
    points.append((x_center - x, y_center - y))  
    points.append((x_center + y, y_center + x)) 
    points.append((x_center - y, y_center + x)) 
    points.append((x_center + y, y_center - x)) 
    points.append((x_center - y, y_center - x)) 

def midpoint_circle (x_center, y_center, r):
    points =[]
    x = 0
    y= r
    d= 1-r
    plot_circle_points(x_center, y_center, x, y,points )
    while x <= y:
        x += 1
        if d<0:
            d = d + 2*x + 1
        else:
            y -= 1
            d= d + 2*x - 2*y + 1
        plot_circle_points(x_center, y_center, x, y, points)

    return points


x_center, y_center = 1,2
radius = 30
point = midpoint_circle(x_center, y_center, radius)
print(point)
x_cord , y_cord = zip(*point)
T = np.array([[1, 0, 1], [0, 1, 2], [0, 0, 1]])
T1 = np.array([[1, 0, -1], [0, 1, -2], [0, 0, 1]])
S = np.array([[5, 0, 0], [0, 3, 0], [0, 0, 1]])


CM = T @ S @ T1
p1 = np.vstack([x_cord, y_cord, np.ones_like(x_cord)])
newmat = CM @ p1
x_coords1, y_coords1 = newmat[0], newmat[1]

print(x_coords1, y_coords1)
plt.scatter(x_coords1, y_coords1,marker="x", color="black" )

plt.scatter(x_cord, y_cord, marker='x')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title("Midpoint circle algorithm")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



