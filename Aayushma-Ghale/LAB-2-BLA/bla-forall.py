import matplotlib.pyplot as plt

def bla():
    # Input the coordinates of the starting and ending points for the line
    x0 = int(input('Enter the value of x0: '))
    y0 = int(input('Enter the value of y0: '))
    x1 = int(input('Enter the value of x1: '))
    y1 = int(input('Enter the value of y1: '))

    # Calculate the differences in x and y
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    # Calculate the slope
    m = dy / dx if dx != 0 else 0  # Prevent division by zero for vertical lines

    # Determine the direction of movement for both x and y
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    # Initialize the decision parameter and plot points
    xplot = [x0]
    yplot = [y0]

    if abs(m) <= 1:  # Shallow slope (|m| <= 1)
        p = 2 * dy - dx  # Initial decision parameter

        # Loop to calculate and plot the points for shallow slope
        while x0 != x1:
            if p >= 0:
                y0 += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
            x0 += sx
            xplot.append(x0)
            yplot.append(y0)

    else:  # Steep slope (|m| > 1)
        p = 2 * dx - dy  # Initial decision parameter

        # Loop to calculate and plot the points for steep slope
        while y0 != y1:
            if p >= 0:
                x0 += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx
            y0 += sy
            xplot.append(x0)
            yplot.append(y0)

    # Plot the line using the collected points
    plt.plot(xplot, yplot, marker='*')
    plt.show()

# Call the function to run the program
bla()
