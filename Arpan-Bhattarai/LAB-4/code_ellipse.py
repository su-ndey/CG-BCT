import matplotlib.pyplot as plt

# Get user input
rx = int(input("Enter the radii rx: "))
ry = int(input("Enter the radii ry: "))
xc = int(input("Enter the ellipse center x-coordinate: "))
yc = int(input("Enter the ellipse center y-coordinate: "))

def ELLIPSE(rx, ry, xc, yc):
    xo, yo = 0, ry
    xes, yes = [], []
    
    # Region 1
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    while 2 * ry**2 * xo <= 2 * rx**2 * yo:
        xes.extend([xo + xc, -xo + xc, xo + xc, -xo + xc])
        yes.extend([yo + yc, yo + yc, -yo + yc, -yo + yc])
        if p1 < 0:
            xo += 1
            p1 += 2 * ry**2 * xo + ry**2
        else:
            xo += 1
            yo -= 1
            p1 += 2 * ry**2 * xo - 2 * rx**2 * yo + ry**2
    
    # Region 2
    p2 = (ry**2 * (xo + 0.5)**2) + (rx**2 * (yo - 1)**2) - (rx**2 * ry**2)
    while yo >= 0:
        xes.extend([xo + xc, -xo + xc, xo + xc, -xo + xc])
        yes.extend([yo + yc, yo + yc, -yo + yc, -yo + yc])
        if p2 > 0:
            yo -= 1
            p2 -= 2 * rx**2 * yo + rx**2
        else:
            xo += 1
            yo -= 1
            p2 += 2 * ry**2 * xo - 2 * rx**2 * yo + rx**2
    
    # Plotting the points
    plt.scatter(xes, yes, s=5, color='blue')

# Call the function
ELLIPSE(rx, ry, xc, yc)

# Display the plot
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
