#midpoint circle drawing algorithm
import matplotlib.pyplot as plt
def lab3():
  x=0
  r=int(input("enter the radius of the circle: "))
  xc=int(input("enter the x-coordinate of circle:"))
  yc=int(input("enter the y-coordinate of circle:"))
  y=r
  p=1-r #initial decision parameter
  xes=[x+xc]
  yes=[y+yc]
  xes.extend([x+xc,-x+xc,x+xc,-x+xc,y+xc,-y+xc,y+xc,-y+xc])
  yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
  while x<y:
    x=x+1
    if p<0:
      p=p+(2*x)+1
    else:
      y=y-1
      p=p+(2*x)-(2*y)+1
    xes.extend([x+xc,-x+xc,x+xc,-x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    plt.scatter(xes,yes)
    plt.show()
lab3()
