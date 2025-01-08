import matplotlib.pyplot as plt

# Taking Inputs from the user
x1 = int(input("Enter x coordinate for the starting point: "))
y1 = int(input("Enter y coordinate for the starting point: "))
x2 = int(input("Enter x coordinate for the ending point: "))
y2 = int(input("Enter y coordinate for the ending point: "))

# Calculate differences
dx = abs(x2 - x1)
dy = abs(y2 - y1)

# Determine step directions
sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

# Initialize decision parameters based on dominant axis
points = []
if dx >= dy:  # Shallow slope (|m| ≤ 1)
    p = 2 * dy - dx
    x, y = x1, y1
    for i in range(dx + 1):  # Include the endpoint
        points.append((x, y))
        x += sx
        if p >= 0:
            y += sy
            p += 2 * (dy - dx)
        else:
            p += 2 * dy
else:  # Steep slope (|m| > 1)
    p = 2 * dx - dy
    x, y = x1, y1
    for i in range(dy + 1):  # Include the endpoint
        points.append((x, y))
        y += sy
        if p >= 0:
            x += sx
            p += 2 * (dx - dy)
        else:
            p += 2 * dx

# Extract x and y coordinates for plotting
x_list, y_list = zip(*points)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_list, y_list, marker='o', color='blue', label='Line Path')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
