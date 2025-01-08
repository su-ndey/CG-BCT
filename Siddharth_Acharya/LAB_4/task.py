import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Take inputs for the center point and radii
xc = int(input("Enter x-coordinate for the center point: "))
yc = int(input("Enter y-coordinate for the center point: "))
rx = int(input("Enter x-radius of the ellipse: "))
ry = int(input("Enter y-radius of the ellipse: "))

# Initialize lists for ellipse points
xes, yes = [], []

# Function to add symmetric points
def add_ellipse_points(xc, yc, x, y):
    xes.extend([xc + x, xc - x, xc + x, xc - x])
    yes.extend([yc + y, yc + y, yc - y, yc - y])

# Initialize variables for Region 1
x, y = 0, ry
rx2, ry2 = rx ** 2, ry ** 2
p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
dx, dy = 2 * ry2 * x, 2 * rx2 * y

# Add initial points for Region 1
add_ellipse_points(xc, yc, x, y)

# Midpoint Ellipse Algorithm - Region 1
while dx < dy:
    x += 1
    dx += 2 * ry2
    if p1 < 0:
        p1 += dx + ry2
    else:
        y -= 1
        dy -= 2 * rx2
        p1 += dx - dy + ry2
    add_ellipse_points(xc, yc, x, y)

# Initialize variables for Region 2
p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

# Midpoint Ellipse Algorithm - Region 2
while y >= 0:
    y -= 1
    dy -= 2 * rx2
    if p2 > 0:
        p2 -= dy + rx2
    else:
        x += 1
        dx += 2 * ry2
        p2 += dx - dy + rx2
    add_ellipse_points(xc, yc, x, y)

# Plot the ellipse points
plt.figure(figsize=(6, 6))  # Set figure size to ensure proper scaling
plt.scatter(xes, yes, color='blue', marker='3')  # Plot ellipse points

plt.gca().set_aspect('equal', adjustable='box')  # Keep aspect ratio equal
plt.title("Ellipse using Midpoint Algorithm")
plt.show()
