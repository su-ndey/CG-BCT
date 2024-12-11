import matplotlib.pyplot as plt

rx=int(input("Enter the radius of the ellipse along x-axis: "))
ry=int(input("Enter the radius of the ellipse along y-axis: "))
xc=int(input("Enter the x coordinate of the center: "))
yc=int(input("Enter the y coordinate of the center: "))

def midpoint_ellipse(rx,ry,xc,yc):
    x=0
    y=ry
    xes=[]
    yes=[]
    p1=(ry**2)-(rx**2)*ry+(rx**2)/4

    while 2*ry**2*x <= 2*rx**2*y:
        xes=[x+xc,-x+xc,x+xc,-x+xc]
        yes=[y+yc,y+yc,-y+yc,-y+yc]
        plt.scatter(xes,yes)
        if p1<0:
            x+=1
            p1=p1+2*ry**2*x+ry**2
        else:
            x+=1
            y-=1
            p1=p1+2*ry**2*x-2*rx**2*y+ry**2
    p2=(ry**2*(x+0.5)**2)+(rx**2*(y-1)**2)-(rx**2*ry**2)
    while y>=0:
        xes=[x+xc,-x+xc,x+xc,-x+xc]
        yes=[y+yc,y+yc,-y+yc,-y+yc]
        plt.scatter(xes,yes)
        if p2>0:
            y-=1
            p2-=2*rx**2*y+rx**2
        else:
            x+=1
            y-=1
            p2+=2*ry**2*x-2*rx**2*y+rx**2
midpoint_ellipse(rx,ry,xc,yc)
plt.show()
    