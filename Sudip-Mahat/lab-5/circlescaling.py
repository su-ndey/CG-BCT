import matplotlib.pyplot as plt
import  numpy as np
xc,yc = map(int,input("Enter centre coordinates :").split(','))
r = int(input("Enter radius :"))
sx,sy = map(int,input("Enter scaling factor for x and y :").split(','))
x=0
y=r
p = 1-r
xes =[]
yes = []
def symmetry_plot(xes,yes,x,y,xc,yc):
    xes.extend([x + xc, -x + xc, x + xc, -x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])
symmetry_plot(xes,yes,x,y,xc,yc)
while x<y:
    x+=1
    if p<0:
        p = p+2*x+1
    else:
        y -=1
        p = p+2*(x-y) +1
        symmetry_plot(xes,yes,x,y,xc,yc)
t = np.array([[1,0,-xc],[0,1,-yc],[0,0,1]])
s = np.array([[sx,0,0],[0,sy,0],[0,0,1]])
T = np.array([[1,0,xc],[0,1,yc],[0,0,1]])
CM = T@s@t
points = np.vstack([xes,yes,np.ones_like(xes)])
TP = CM@points
plt.figure(figsize=(6,5))
plt.scatter(xes, yes, label='Original Circle')
plt.scatter(TP[0], TP[1], color='black', label='Transformed Circle')
plt.title("Midpoint Circle Drawing with Transformations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc='center')
plt.grid()
plt.savefig('output for circle scaling.png')
plt.show()