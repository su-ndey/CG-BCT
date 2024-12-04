import matplotlib.pyplot as plt
def bla():
    x1 = int(input('enter the value of x1:'))
    y1 = int (input('enter the value of y1:'))
    x2 = int (input('enter the value of x2:'))
    y2 = int (input('enter the value of y2:'))
    
    dx = abs(x2 -x1)
    dy = abs(y2- y1)
    xes =[x1]
    yes =[y1]
    k = 0 
    p = 2*dy - dx
    x= x1
    y=y1
    while(x<=x2):
        if (p < 0):
            xes.append(x)
            yes.append(y)
            x=x+1

            p = p + 2*dy
        else:
            xes.append(x)
            yes.append(y)
            x=x+1
            y+=1

            p = p + 2*dy -2*dx
         
    plt.plot(xes,yes,marker='*')
    plt.show()
bla()   



        




    
    

    