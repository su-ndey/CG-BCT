# Mid circle drawing algorithm
import matplotlib.pyplot as plt
r = int(input("radius of the circle is:"))
xc= int(input("x coordinate of centre is:"))
yc= int(input("y coordinate of centre is:"))
x=0
y=r 
p=1-r
xes=[]
yes=[]
xes.append(0+xc)
yes.append(r+yc)
     
xes.append(x+xc)
yes.append(y+yc)

xes.append(-x+xc)
yes.append(y+yc)

xes.append(-x+xc)
yes.append(-y+yc)

xes.append(x+xc)
yes.append(-y+yc)

xes.append(y+xc)
yes.append(x+yc)

xes.append(-y+xc)
yes.append(x+yc)

xes.append(y+xc)
yes.append(-x+yc)

xes.append(-y+xc)
yes.append(-x+yc)
while (x<y):
    x=x+1
    if p< 0:
        p=p+2*x+1
    else:
        y=y-1
        p=p+2*(x-y)+1
        xes.append(x+xc)
        yes.append(y+yc)

        xes.append(-x+xc)
        yes.append(y+yc)

        xes.append(-x+xc)
        yes.append(-y+yc)

        xes.append(x+xc)
        yes.append(-y+yc)

        xes.append(y+xc)
        yes.append(x+yc)

        xes.append(-y+xc)
        yes.append(x+yc)

        xes.append(y+xc)
        yes.append(-x+yc)

        xes.append(-y+xc)
        yes.append(-x+yc)

plt.scatter(xes, yes, color='blue', s=10)
plt.title("Midpoint Circle Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()