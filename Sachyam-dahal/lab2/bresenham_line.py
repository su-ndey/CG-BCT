import matplotlib.pyplot as plt
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



line_points = bresenham_line(10, 7, -1, -6)
for point in line_points:
    print(point)
x_coords , y_coords = zip(*line_points)
plt.plot(x_coords, y_coords,marker="x", color="black" )
plt.title("BLA")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
