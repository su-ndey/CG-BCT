import matplotlib.pyplot as plt
rx=int(input("enter the radius of rx : "))
ry=int(input("enter the radius of ry : "))
xc=int(input("enter the center of xc : "))
yc=int(input("enter the center of yc : "))

def mid(rx,ry,xc,yc):
    x=0
    y=ry
    xes=[]
    yes=[]
    p1=(ry**2)-(rx**2*ry)+1/4*(rx**2)
    while (2*ry**2*x) <= (2*rx**2*y):
        xes.extend([x+xc, -x+xc, x+xc, -x+xc])
        yes.extend([y+yc, y+yc, -y+yc, -y+yc])
        if p1 < 0:
            x += 1
            p1 += 2*ry**2*x + ry**2
        else:
            x += 1
            y -= 1
            p1 += 2*ry**2*x - 2*rx**2*y + ry**2
    p2 = (ry**2 * (x + 0.5) ** 2) + (rx**2 * (y - 1) ** 2) - (rx**2 * ry**2)
    while y>=0:
        xes.extend([x+xc, -x+xc, x+xc, -x+xc])
        yes.extend([y+yc, y+yc, -y+yc, -y+yc])
        if p2 > 0:
            y -= 1
            p2 -= 2*rx**2 * y + rx**2
        else:
            x +=1
            y -= 1
            p2 += 2*ry**2 * x - 2*rx**2 * y + rx**2
    plt.scatter(xes ,yes ,marker='o')
mid(rx, ry, xc, yc)
plt.title("Midpoint Algorithm of Ellipse")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()