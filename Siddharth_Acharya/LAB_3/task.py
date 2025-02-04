import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Take inputs for the center point and radius
xc = int(input("Enter x-coordinate for the center point: "))
yc = int(input("Enter y-coordinate for the center point: "))
r = int(input("Enter the radius: "))

# Initialize lists for circle points
xes, yes = [], []

# Initialize variables
x, y = 0, r
p = 1 - r

# Function to add symmetric points
def add_circle_points(xc, yc, x, y):
    xes.extend([xc + x, xc - x, xc + y, xc - y, xc + x, xc - x, xc + y, xc - y])
    yes.extend([yc + y, yc + y, yc + x, yc + x, yc - y, yc - y, yc - x, yc - x])

# Add initial points
add_circle_points(xc, yc, x, y)

# Midpoint Circle Algorithm
while x < y:
    x += 1
    if p < 0:
        p += 2 * x + 1
    else:
        y -= 1
        p += 2 * x - 2 * y + 1
    add_circle_points(xc, yc, x, y)

# Zip the points into x_list and y_list
x_list, y_list = zip(*sorted(zip(xes, yes)))

# Plot the circle points
plt.figure(figsize=(6, 6))  # Set figure size to ensure it doesn't look like an ellipse
plt.scatter(x_list, y_list, color='blue', marker='3')  # Join points with lines
plt.gca().set_aspect('equal', adjustable='box')  # Keep aspect ratio equal
plt.title("Circle using Midpoint Algorithm")
plt.show()

