#midpoint circle drawing algorithm
import matplotlib.pyplot as plt

r= int(input("enter radius: "))
xc=int(input("Enter x coordinate of center: "))
yc=int(input("Eneter y coordinate of center:"))

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
    if(p<0):
        p=p+2*x+1
    if(p>=0):
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
               
print(f' {xes},{yes}   ')
plt.scatter(xes,yes,marker="*")
plt.show()








                   
                   

        
        

    

   



  



