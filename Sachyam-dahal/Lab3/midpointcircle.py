import matplotlib.pyplot as plt
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
x_cord , y_cord = zip(*point)
plt.scatter(x_cord, y_cord, marker='x')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.title("Midpoint circle algorithm")
plt.xlabel("x")
plt.ylabel("y")
plt.show()