import matplotlib.pyplot as plt

def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry
    points = []
    
    def plot_symmetry(x, y):
        points.extend([
            (x + xc, y + yc), (-x + xc, y + yc),
            (x + xc, -y + yc), (-x + xc, -y + yc)
        ])

    P1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y
    plot_symmetry(x, y)

    while dx < dy:
        if P1 < 0:
            x += 1
            dx = 2 * ry**2 * x
            P1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            P1 += dx - dy + ry**2
        plot_symmetry(x, y)


    P2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)
    while y > 0:
        if P2 > 0:
            y -= 1
            dy = 2 * rx**2 * y
            P2 -= dy + rx**2
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            P2 += dx - dy + rx**2
        plot_symmetry(x, y)

    return points

xc, yc, rx, ry = 200, 100, 200, 100  
ellipse_points = midpoint_ellipse(rx, ry, xc, yc)


x_coords, y_coords = zip(*ellipse_points)




plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, c='lavender', s=10)  
plt.title("Midpoint Ellipse Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')  
plt.grid(True)
plt.show()

