import matplotlib.pyplot as plt

# Taking Inputs from the user
xc = int(input("Enter x coordinate for the center point: "))
yc = int(input("Enter y coordinate for the center point: "))
r = int(input("Enter the radius: "))


xes = []
yes = []

x = 0
y = r
p = 1 - r


def add_circle_points(xc, yc, x, y):
    # For xes
    xes.append(xc + x)  # 1st point
    xes.append(xc - x)  # 2nd point
    xes.append(xc + y)  # 3rd point
    xes.append(xc - y)  # 4th point
    xes.append(xc + x)  # 5th point (repeated for symmetry)
    xes.append(xc - x)  # 6th point (repeated for symmetry)
    xes.append(xc + y)  # 7th point (repeated for symmetry)
    xes.append(xc - y)  # 8th point (repeated for symmetry)

    # For yes
    yes.append(yc + y)  # 1st point
    yes.append(yc + y)  # 2nd point (repeated for symmetry)
    yes.append(yc + x)  # 3rd point
    yes.append(yc + x)  # 4th point (repeated for symmetry)
    yes.append(yc - y)  # 5th point
    yes.append(yc - y)  # 6th point (repeated for symmetry)
    yes.append(yc - x)  # 7th point
    yes.append(yc - x)  # 8th point (repeated for symmetry)


# Initial point
add_circle_points(xc, yc, x, y)

# Midpoint circle algorithm
while x < y:
    x += 1
    if p < 0:
        p += 2 * x + 1
    else:
        y -= 1
        p += 2 * x - 2 * y + 1
    add_circle_points(xc, yc, x, y)


    

# Plotting the circle
plt.figure(figsize=(6, 6))
plt.scatter(xes, yes, color='blue', marker='3')

plt.xlim(xc - r - 1, xc + r + 1)
plt.ylim(yc - r - 1, yc + r + 1)


plt.show()