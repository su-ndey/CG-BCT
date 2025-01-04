import matplotlib.pyplot as plt

def midpoint_ellipse(rx, ry, xc, yc):
    # Initialize variables
    x = 0
    y = ry
    
    xs = []
    ys = []
    
    # Initial decision parameter for region 1
    p1 = ry * ry - (rx * rx * ry) + (0.25 * rx * rx)
    
    # Iterate through region 1
    while (2 * ry * ry * x <= 2 * rx * rx * y):
        # Plot points for all four quadrants
        xs.append(x + xc)
        ys.append(y + yc)

        xs.append(-x + xc)
        ys.append(y + yc)
        
        xs.append(x + xc)
        ys.append(-y + yc)

        xs.append(-x + xc)
        ys.append(-y + yc)

        if p1 < 0:
            x = x + 1
            p1 = p1 + 2 * ry * ry * x + ry * ry
        else:
            x = x + 1
            y = y - 1
            p1 = p1 + 2 * ry * ry * x - 2 * rx * rx * y + ry * ry

    # Initial decision parameter for region 2
    p2 = (ry * ry * (x + 0.5) * (x + 0.5)) + (rx * rx * (y - 1) * (y - 1)) - (rx * rx * ry * ry)
    
    # Iterate through region 2
    while (y >= 0):
        # Plot points for all four quadrants
        xs.append(x + xc)
        ys.append(y + yc)
        
        xs.append(-x + xc)
        ys.append(y + yc)
        
        xs.append(x + xc)
        ys.append(-y + yc)
        
        xs.append(-x + xc)
        ys.append(-y + yc)

        if p2 > 0:
            y = y - 1
            p2 = p2 - 2 * rx * rx * y + rx * rx
        else:
            x = x + 1
            y = y - 1
            p2 = p2 + 2 * ry * ry * x - 2 * rx * rx * y + rx * rx

    # Plot the ellipse
    plt.scatter(xs, ys, marker="o", color="blue")
    plt.title("Midpoint Ellipse Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

# Parameters for the ellipse (center, rx, ry)
xc, yc = 100, 99
rx, ry = 50, 56
midpoint_ellipse(rx, ry, xc, yc)

   

   





