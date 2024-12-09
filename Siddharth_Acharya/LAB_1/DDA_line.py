import matplotlib.pyplot as plt

# Get inputs and convert to integers
x1 = int(input("Enter x coordinate for first point: "))
y1 = int(input("Enter y coordinate for first point: "))
x2 = int(input("Enter x coordinate for second point: "))
y2 = int(input("Enter y coordinate for second point: "))

# Calculate differences
dx = abs(x2 - x1)
dy = abs(y2 - y1)

# Determine the number of steps
steps = int(max(dx, dy))

# Calculate increments
x_incr = dx / steps
y_incr = dy / steps

# Initialize starting point
x = x1
y = y1

# Lists to store points
x_list = [x]
y_list = [y]

# Generate points
for i in range(steps):
    x += x_incr
    y += y_incr
    x_list.append(round(x))  # Round to the nearest integer
    y_list.append(round(y))  # Round to the nearest integer

# Print the lists of points
print(x_list)
print(y_list)

# Print the starting point
print(f"The Starting Point is {x1},{y1}")

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(x_list, y_list, marker='o', color='blue', label='Line Path')
plt.scatter([x1, x2], [y1, y2], color='red', label='Start & End Points')  # Highlight start and end points
plt.title("Line Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()