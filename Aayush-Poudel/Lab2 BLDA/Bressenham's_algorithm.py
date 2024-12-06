import matplotlib.pyplot as plt

def BA():
    x1=int(input('Enter the value of x1: '))
    y1=int(input('Enter the value of y1: '))
    x2=int(input('Enter the value of x2: '))
    y2=int(input('Enter the value of y2: '))

    dx=abs(x2-x1)
    dy=abs(y2-y1)

    xes=[]
    yes=[]
    x,y = x1,y1
    if(dx>=dy):
        
        if(x2>x1):
            sx=1
        else:
            sx=-1    
        if(y2>y1):
            sy=1
        else:
            sy=-1
        k=0
        Po=(2*dy)-dx
        Pk=Po
        while(x<x2):
            xes.append(x)
            yes.append(y)
            x=x+sx
            if(Pk>=0):
                y=y+sy
                pkk=Pk+2*dy-2*dx
            else:
                pkk=Pk+2*dy
    if(dy>=dx):
        
        if(x2>x1):
            sx=1
        else:
            sx=-1    
        if(y2>y1):
            sy=1
        else:
            sy=-1
        k=0
        Po=(2*dx)-dy
        Pk=Po
        while(x<x2):
            xes.append(x)
            yes.append(y)
            y=y+sy
            if(Pk>=0):
                x=x+sx
                pkk=Pk+2*dx-2*dy
            else:
                pkk=Pk+2*dx
    plt.plot(xes, yes, marker='x')
    plt.show()

BA()
