import matplotlib.pyplot as plt

def symmetry_plotter(xes,yes,x,y,xc,yc): #plot function
        xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+yc,-y+yc,y+yc,-y+yc])
        yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+xc,x+xc,-x+xc,-x+xc])

xc= int(input("enter x-coordinate: "))
yc= int(input("enter y-coordinate: "))
r= int(input("enter the radius of  the circle: "))

p=1-r #initial parameter
xes=[]
x,y = 0, r
yes=[]

symmetry_plotter(xes,yes,x,y,xc,yc)

while x<y:
    x=x+1
    if p<0:
        p=p+2*x+1
    else:
        y=y-1
        p=p+2*(x-y)+1
    symmetry_plotter(xes,yes,x,y,xc,yc)
plt.figure(figsize=(6,6))
plt.scatter(xes, yes, marker='.', color='teal')
plt.title("Circle Drawing")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
