# midpoint ellipse algorithm
import matplotlib.pyplot as plt
rx = int(input("radius of the ellipse in x coordinate is:"))
ry = int(input("radius of the ellipse in y coordinate is:"))
xc= int(input("x coordinate of ellipse centre is:"))
yc= int(input("y coordinate of ellipse centre is:"))
def plot(x,y):
    plt.plot(x,y,marker='o')
def MPE(rx,ry,xc,yc):
    x = 0
    y = ry
    r1 = ry*ry
    r2 = rx*rx
    p1 = r1 - r1*ry + 0.25*r2
    while (2*r1*x <= 2*r2*y):
        plot(x+xc, y+yc)
        plot(-x+xc, y+yc)
        plot(x+xc, -y+yc)
        plot(-x+xc, -y+yc)
        if (p1 < 0):
            x += 1
            p1 += 2*r1*x + r1
        else:
            x += 1
            y -= 1
            p1 += 2*r1*x - 2*r2*y + r1
    p2 = (r1 * (x + 0.5) ** 2) + (r2 * (y - 1) ** 2) - (r2 * r1)
    while y >= 0:
        plot(x + xc, y + yc)
        plot(-x + xc, y + yc)
        plot(x + xc, -y + yc)
        plot(-x + xc, -y + yc)
        if (p2 > 0):
            y -= 1
            p2 -= 2*r2 * y + r2
        else:
            x += 1
            y -= 1
            p2 += 2*r1 * x - 2*r2 * y + r2
    plt.scatter(x, y, color='blue', s=10)
    plt.title("Midpoint Ellipse Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()
MPE(rx,ry,xc,yc)

                        
         
        
                    
                        
