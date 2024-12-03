#Bresenham algorithm

import matplotlib.pyplot as plt
def BHM_algorithm(x1,y1,x2,y2):
    

    dx=x2-x1
    dy=y2-y1
    
    x,y=x1,y1

    dx,dy=abs(dx),abs(dy)
    xes=[]
    yes=[]
    
    if dx>=dy:
        Pk=2*dy-dx

        #steps 
        if dx>0:
           steps_x=1
        else:
            steps_x=-1
        if dy>0:
            steps_y=1
        else:
            steps_y=-1

    else:  
     Pk=2*dx-dy


    for i in range(x1,x2):
        x=x+steps_x
        if Pk>=0:
         y=y+steps_y

         Pkn=Pk+2*dy-2*dx
        else:
           Pkn=Pk+2*dy
        xes.append(x)
        yes.append(y)
        
    plt.plot(xes,yes,marker='*') 
    plt.show()  

x1=int(input('enter the number: '))
y1=int(input('enter the number: '))
x2=int(input('enter the number: '))
y2=int(input('enter the number: '))       

BHM_algorithm(x1,y1,x2,y2)

    