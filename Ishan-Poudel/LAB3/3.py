import matplotlib.pyplot as plt
xes= []
yes=[]
x=0
r= int(input("Enter the radius: \n"))
y=r
xc= int(input("Enter the centre point x: \n"))
yc= int(input("Enter the centre point y: \n"))
xes.append(x+xc)
yes.append(y+yc)


#xes.append(xc)

#yes.append(yc)


p=1-y #initial parameter


while (x<y):
    x=x+1
    if p<0:
        p=p+2*x+1
    else:
        y=y-1
        p=p+2*(x-y)+1
    a=x+xc
    b=y+yc
    xes.extend([a,-a,-a,a,b,-b,b,-b])
    yes.extend([b,b,-b,-b,a,a,-a,-a])
    print({x},{y}) 


plt.scatter(xes, yes, color='black',marker='o')
plt.grid()
plt.show()