import matplotlib.pyplot as plt
def plot(x, y):
    plt.scatter(x, y, color='black')
def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    
    while two_ry2 * x <= two_rx2 * y:
       
        plot(x + xc, y + yc)
        plot(-x + xc, y + yc)
        plot(x + xc, -y + yc)
        plot(-x + xc, -y + yc)

       
        if p1 < 0:
            x += 1
            p1 += two_ry2 * x + ry2
        else:
            x += 1
            y -= 1
            p1 += two_ry2 * x - two_rx2 * y + ry2

    
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

  
    while y >= 0:
        
        plot(x + xc, y + yc)
        plot(-x + xc, y + yc)
        plot(x + xc, -y + yc)
        plot(-x + xc, -y + yc)

        
        if p2 > 0:
            y -= 1
            p2 -= two_rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += two_ry2 * x - two_rx2 * y + rx2


rx = int(input("Enter the (rx): "))
ry = int(input("Enter the (ry): "))
xc = int(input("Enter the x-coordinate of the center (xc): "))
yc = int(input("Enter the y-coordinate of the center (yc): "))

midpoint_ellipse(rx, ry, xc, yc)
plt.grid(True)
plt.show()
