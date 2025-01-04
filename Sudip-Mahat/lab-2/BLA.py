import matplotlib.pyplot as plt
# Function to plot the points
def Bresen():
    # Input the points
    x0 = int(input("Enter the point x0: "))
    y0 = int(input("Enter the point y0: "))
    x1 = int(input("Enter the point x1: "))
    y1 = int(input("Enter the point y1: "))

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1
# List to store the points
    xes = [x0]
    yes = [y0]

    if dx > dy:
        p = 2 * dy - dx
        while x0 != x1:
            x0 = x0 + sx
            if p >= 0:
                y0 = y0 + sy
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            xes.append(x0)
            yes.append(y0)
    else:
        p = 2 * dx - dy
        while y0 != y1:
            y0 = y0 + sy
            if p >= 0:
                x0 = x0 + sx
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
            xes.append(x0)
            yes.append(y0)
    
    # Ploting  the points
    plt.plot(xes, yes, marker='*', color='yellow')
    plt.show()

# Calling the  function
Bresen()