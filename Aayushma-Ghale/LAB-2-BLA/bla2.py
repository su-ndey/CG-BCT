import matplotlib.pyplot as plt
def bla():
    x0 = int(input('enter the value of x0:'))
    y0 = int(input('enter the value of y0:'))
    x1 = int(input('enter the value of x1:'))
    y1 = int(input('enter the value of y1:'))
    
    dx = abs(x1 -x0)
    dy = abs(y1- y0)
    xes =[x0]
    yes =[y0]
    
    if  (x1> x0):
         Sx = 1
    else:
        Sx = -1
    
    if(y1> y0):
        Sy = 1
    else:
        Sy = -1 

    
    if (dx>=dy):
        while(x0!=x1):
            x0 = x0 + Sx
            if(p>=0):
                y0 = y0 + Sy
                p = p + 2*dy-2*dx
            else:
                p=p+2*dy
        
    if (dx <dy):
        if (p >=0):
            x=x+Sx
            p = p + 2*dy -2*dx
        else:
            p = p + 2*dy 
        

        plt.plot(xes,yes,marker='*')
        plt.show()


bla()       



   