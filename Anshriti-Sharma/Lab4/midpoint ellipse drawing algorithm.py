#midpoint ellipse drawing algorithm
import matplotlib.pyplot as plt

rx=int(input("Enter major axis:"))
ry=int(input("Enter minor axis:"))
xc=int(input("Enter x coordinate of center:"))
yc=int(input("Enter y coordinate of center:"))

x=0
y=ry

#for decision parameter
p1=ry*ry-(rx*rx*ry) + (0.25*rx*rx)

xes = []
yes = []

#for region 1
while(2*ry*ry*x<=2*rx*rx*y):
    if (p1<0):
        x=x+1
        p1=p1+2*ry*ry*x+ry*ry
    else:
        x=x+1
        y=y-1
        p1=p1+ry*ry*x-2*rx*rx*y+ry*ry

        xes.append(x + xc)
        yes.append(y + yc)
        xes.append(-x + xc)
        yes.append(y + yc)
        xes.append(x + xc)
        yes.append(-y + yc)
        xes.append(-x + xc)
        yes.append(-y + yc)

#for region 2
#decision parameter
p2=(ry*ry*(x+0.5)**2)+(rx*rx*(y-1)**2)-(rx*rx*ry*ry)
while(y>=0):
     if (p2>0):
         y=y-1
         p2=p2-2*rx*rx*y+rx*rx
     else:
          x=x+1
          y=y-1
          p2=p2+2*ry*ry*x-2*rx*rx*y+rx*rx

          xes.append(x + xc)
          yes.append(y + yc)
          xes.append(-x + xc)
          yes.append(y + yc)
          xes.append(x + xc)
          yes.append(-y + yc)
          xes.append(-x + xc)
          yes.append(-y + yc)

print(f' {xes},{yes}   ')
plt.scatter(xes,yes,marker="*")
plt.show()
