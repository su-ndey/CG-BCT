import matplotlib.pyplot as plt
def plot(x,y,xc,yc,xes,yes):
    
    xes.extend([x+xc, -x+xc, -x+xc, x+xc, y+xc, -y+xc, y+xc,-y+xc])
    yes.extend([y+yc, y+yc, -y+yc, -y+yc,x+xc,x+xc,-x+xc,-x+xc])

x=0
xc=int(input('Enter the value of xc='))
yc=int(input('Enter the value of yc='))
r=int(input('Enter the value of radius='))
y=r

p=1-r
xes=[]
yes=[]
plot(x,y,xc,yc,xes,yes)
while x<y:
    x=x+1
    if p<0:
        p=p+2*x+1
    else:
        y=y-1
        p=p+2*(x-y)+1

    plot(x,y,xc,yc,xes,yes)

plt.scatter(xes, yes)
plt.gca().set_aspect('equal' ,adjustable ='box')
plt.grid(True)
plt.show()
        
