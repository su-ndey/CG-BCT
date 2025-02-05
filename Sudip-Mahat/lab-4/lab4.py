import matplotlib.pyplot as plt
xc,yc = map(int,input("Enter center coordinate :").split(','))
a,b = map(int,input("Enter value for rx and ry :").split(','))
x = 0
y = b
P = b**2 - a**2 *b +0.25*a**2
xes =[]
yes = []
def symmetry_plot():
    xes.extend([x+xc,-x+xc,x+xc,-x+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc])
while (2*x*b**2 <= 2*y*a**2):
    symmetry_plot()
    if P<0:
        x +=1
        P += 2*x*b**2 + b**2
    else:
        x += 1
        y = y-1
        P = 2*x*(b**2) - 2*y*(a**2) + b**2
P =  ((x+0.5)**2)*(b**2) + (a**2)*(y-1)**2 - (a**2)*b**2
    
while y>=0:
    symmetry_plot()
    if P > 0:
        y -= 1
        P += -2*y*(a**2) - a**2
    else:
        x +=1
        y -= 1
        P += 2*x*(b**2)-2*y*(a**2) - a**2
plt.figure(figsize=(10,5))
plt.scatter(xes,yes,color="red")
plt.title("Midpoint Ellipse Drawing Algorithm")
plt.savefig("output2.png")
plt.grid()
plt.show()