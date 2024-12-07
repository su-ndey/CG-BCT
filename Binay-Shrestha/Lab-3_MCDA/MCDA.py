# Midpoint Circle Drawing Algorithm

import matplotlib.pyplot as plt

x =0
r =int(input("Enter the radius of the circle: "))
xc= int(input("Enter the x coordinate of the center: "))
yc= int(input("Enter the y coordinate of the center: "))
y =r
p =1-r
xes =[]
yes =[]
def plot(x,y,xc,yc):
    xes.extend([x+ xc, -x+ xc, x+ xc, -x+ xc, y+ xc, -y+ xc, y+ xc, -y+ xc])
    yes.extend([y+ yc, y+ yc, -y+ yc, -y+ yc, x+ yc, -x+ yc, -x+ yc, x+ yc])
plot(x,y,xc,yc)
while x<y:
    x+=1
    if p<0:
        p =p+2*x+1
    else:
        y-=1
        p = p+2*(x-y)+1
    plot(x,y,xc,yc)

plt.scatter(xes,yes)
plt.show()

 


