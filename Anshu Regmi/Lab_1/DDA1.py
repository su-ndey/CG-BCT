#dda algorithm implementation
import matplotlib.pyplot as plt
def dda_algorithm(x1,y1,x2,y2):
    

    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    
    xes=[]
    yes=[]
    xincrement=dx/steps
    yincrement=dy/steps
    
    x,y=x1,y1
    for i in range(steps):
        
        xes.append(x)
        yes.append(y)
        
        x=x1+xincrement
        y=y1+yincrement
    plt.plot(xes,yes,marker='*')
    plt.show()

x1=int(input('enter the number: '))
y1=int(input('enter the number: '))
x2=int(input('enter the number: '))
y2=int(input('enter the number: '))       

dda_algorithm(x1,y1,x2,y2)
