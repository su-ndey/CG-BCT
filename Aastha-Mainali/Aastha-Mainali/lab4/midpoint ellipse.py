#midpoint ellipse drawing algorithm
import matplotlib.pyplot as plt
def lab4(rx,ry,xc,yc):
  x=0
  rx=int(input("enter the radius of the ellipse for x-coordinate: "))
  ry=int(input("enter the radius of the ellipse for y-coordinate: "))
  xc=int(input("enter the x-coordinate of ellipse:"))
  yc=int(input("enter the y-coordinate of ellipse:"))
  y=ry
  p1=ry**2-(rx**2*ry)+(0.25*rx**2)
  while 2*ry**2*x<2*rx**2*y:
    plot(x+xc,y+yc)
    plot(x+xc,-y+yc)
    plot(-x+xc,y+yc)
    plot(-x+xc,-y+yc)
    if p1<0:
      x=x+1
      p1=p1+2*ry**2*x+ry**2
    else:
      x=x+1
      y=y-1
      p1=p1+2*ry**2*x-2*rx**2*y+ry**2
  p2=(ry**2*(x+0.5)**2)+(rx**2*(y-1)**2)-(rx**2*ry**2)
  while y>=0:
    plot(x+xc,y+yc)
    plot(x+xc,-y+yc)
    plot(-x+xc,y+yc)
    plot(-x+xc,-y+yc)
    if p2>0:
      y=y-1
      p2-=2*ry**2*y+rx**2
    else:
      x=x+1
      y=y-1
      p2+=2*ry**2*x-2*rx**2*y+rx**2
def plot(x,y):
  plt.plot(x, y, marker='o', color="red")
lab4(0, 0, 0, 0)
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.show()