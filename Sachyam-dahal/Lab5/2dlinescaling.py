import matplotlib.pyplot as plt
import numpy as np
def bresenham_line(x1, y1, x2, y2):
  

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
 
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

 
    if dx > dy:
     
        p = 2 * dy - dx
        x, y = x1, y1

    
        points = []
        for _ in range(dx + 1):
            points.append((x, y)) 
            if p >= 0:
                y += sy  
                p -= 2 * dx
            x += sx  
            p += 2 * dy
    else:
       
        p = 2 * dx - dy
        x, y = x1, y1

      
        points = []
        for _ in range(dy + 1):
            points.append((x, y))  
            if p >= 0:
                x += sx  
                p -= 2 * dy
            y += sy 
            p += 2 * dx

    return points



line_points = bresenham_line(3,2,5,6)
print(line_points)



T = np.array([[1, 0, 3], [0, 1, 2], [0, 0, 1]])
T1 = np.array([[1, 0, -3], [0, 1, -2], [0, 0, 1]])
S = np.array([[5, 0, 0], [0, 3, 0], [0, 0, 1]])


CM = T @ S @ T1
print(CM)




x_coords, y_coords = zip(*line_points)


p1 = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])


newmat = CM @ p1
print(newmat)


x_coords1, y_coords1 = newmat[0], newmat[1]

print(x_coords1, y_coords1)




T = np.array([[1, 0, 3], [0, 1, 2], [0, 0, 1]])
T1 = np.array([[1, 0, -3], [0, 1, -2], [0, 0, 1]])
S = np.array([[5, 0, 0], [0, 3, 0], [0, 0, 1]])


CM = T @ S @ T1




x_coords, y_coords = zip(*line_points)


p1 = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])


newmat = CM @ p1


x_coords1, y_coords1 = newmat[0], newmat[1]


print(x_coords1, y_coords1)
plt.plot(x_coords1, y_coords1,marker="x", color="black" )
plt.plot(x_coords, y_coords,marker="x", color="black" )
plt.title("BLA")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

