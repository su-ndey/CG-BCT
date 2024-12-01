import matplotlib.pyplot as plt

x1 = input("Enter x coordinate for the starting point: ")
y1 = input("Enter y coordinate for the starting point: ")
x2 = input("Enter x coordinate for the ending point: ")
y2 = input("Enter y coordinate for the ending point: ")

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

points = []
if dx >= dy: 
    p = 2 * dy - dx
    x, y = x1, y1
    for i in range(dx + 1):
        points.append((x, y))
        x += sx
        if p >= 0:
            y += sy
            p += 2 * (dy - dx)
        else:
            p += 2 * dy
else:  
    p = 2 * dx - dy
    x, y = x1, y1
    for i in range(dy + 1): 
        points.append((x, y))
        y += sy
        if p >= 0:
            x += sx
            p += 2 * (dx - dy)
        else:
            p += 2 * dx

x_list, y_list = zip(*points)


plt.figure(figsize=(8, 6))
plt.plot(x_list, y_list, marker='o', color='blue', label='Line Path')
plt.show()