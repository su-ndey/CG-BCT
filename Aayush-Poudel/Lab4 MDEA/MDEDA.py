import matplotlib.pyplot as plt
rx = int(input('Enter the horizontal radius:-'))
ry = int(input('Enter the vertical radius:-'))
xc = int(input('Enter the x coords of center:-'))
yc = int(input('Enter the y coords of center:-'))

def plot(x, y):
    plt.plot(x,y,marker='o')



def midpoint_ellipse(rx, ry, xc, yc):
    # Step 1: Initialize variables
    x = 0
    y = ry
    rx2 = rx * rx 
    ry2 = ry * ry  
    two_rx2 = 2 * rx2  
    two_ry2 = 2 * ry2  

    # Step 2: Region 1 Initial Decision Parameter
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    # Step 3: Iterate through Region 1
    while two_ry2 * x <= two_rx2 * y:
        # Plot points for all four quadrants
        plot(x + xc, y + yc)
        plot(-x + xc, y + yc)
        plot(x + xc, -y + yc)
        plot(-x + xc, -y + yc)

        # Update x and decision parameter
        if p1 < 0:
            x += 1
            p1 += two_ry2 * x + ry2
        else:
            x += 1
            y -= 1
            p1 += two_ry2 * x - two_rx2 * y + ry2

    # Step 4: Region 2 Initial Decision Parameter
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    # Step 5: Iterate through Region 2
    while y >= 0:
        # Plot points for all four quadrants
        plot(x + xc, y + yc)
        plot(-x + xc, y + yc)
        plot(x + xc, -y + yc)
        plot(-x + xc, -y + yc)

        # Update y and decision parameter
        if p2 > 0:
            y -= 1
            p2 -= two_rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += two_ry2 * x - two_rx2 * y + rx2

midpoint_ellipse(rx,ry,xc,yc)
plt.show()