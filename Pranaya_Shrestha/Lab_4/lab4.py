
import matplotlib.pyplot as plt
rx=float(input("Enter radii rx: "))
ry=float(input("Enter radii ry: "))

xc=float(input("Enter the x-coordinate of center of ellipse: "))
yc=float(input("Enter the y-coordinate of center of ellipse: "))

x_coordinates=[]
y_coordinates=[]

x=0
y=ry

def SymmetryPlotter(x_coordinates, y_coordinates, x, y, xc, yc):
    x_coordinates.extend([x + xc, -x + xc, x + xc, -x + xc])
    y_coordinates.extend([y + yc, y + yc, -y + yc, -y + yc])



SymmetryPlotter(x_coordinates,y_coordinates,x,y,xc,yc)

p1=pow(ry,2)-pow(rx,2)*ry+(1/4)*pow(rx,2)

while 2*pow(ry,2)*x<=2*pow(rx,2)*y:
    if p1<0:
        x+=1
        p1=p1+2*pow(ry,2)*x+pow(ry,2)
    else:
        x=x+1
        y=y-1
        p1=p1+2*pow(ry,2)*x-2*pow(rx,2)*y+pow(ry,2)
    SymmetryPlotter(x_coordinates,y_coordinates,x,y,xc,yc)
p2=pow(ry,2)*pow((x+0.5),2)+pow(rx,2)*pow((y-1),2)-rx**2*ry**2

while y>=0:
    if p2>0:
        y-=1
        p2=p2-2*rx**2*y+rx**2
    else:
        x+=1
        y-=1
        p2=p2+2*ry**2*x-2*rx**2*y+rx**2
    SymmetryPlotter(x_coordinates,y_coordinates,x,y,xc,yc)

plt.scatter(x_coordinates,y_coordinates)
plt.show()