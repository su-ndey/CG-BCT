import matplotlib.pyplot as plt
r1 = int(input("Enter first radius: "))
r2 = int(input("Enter second radius: "))
xc = int(input("Enter you x-axis center:"))
yc = int(input("Enter you y-axis center:"))
def elp(r1, r2, xc, yc):
    x = 0
    y = r2
    xes = []
    yes = []
    p1 = (r2**2) - (r1**2*r2) + (1/4)*r1
    while 2*r2**2*x <= 2*r1**2*y:
        xes = [x+xc, -x+xc, x+xc, -x+xc]
        yes = [y+yc, y+yc, -y+yc, -y+yc]
        plt.scatter(xes, yes)
        if p1 < 0:
            x += 1
            p1 += 2*r2**2*x + r2**2
        else:
            x += 1
            y -= 1
            p1 += 2*r2**2*x - 2*r1**2*y + r2**2
    p2 = (r2**2 * (x + 0.5) ** 2) + (r1**2 * (y - 1) ** 2) - (r1**2 * r2**2)
    while y >= 0:
        xes = [x+xc, -x+xc, x+xc, -x+xc]
        yes = [y+yc, y+yc, -y+yc, -y+yc]
        plt.scatter(xes, yes)
        if p2 > 0:
            y -= 1
            p2 -= 2*r1**2 * y + r1**2
        else:
            x +=1
            y -= 1
            p2 += 2*r2**2 * x - 2*r1**2 * y + r1**2

elp(r1, r2, xc, yc)
plt.grid(True)
plt.show()

