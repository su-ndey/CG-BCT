import matplotlib.pyplot as plt
def bla():
    x1 = int(input('enter the value of x1:'))
    y1 = int (input('enter the value of y1:'))
    x2 = int (input('enter the value of x2:'))
    y2 = int (input('enter the value of y2:'))
    
    dx = abs(x2 -x1)
    dy = abs(y2- y1)
    xcoordinate =[x1]
    ycoordinate =[y1]
    k = 0 
    p = 2*dy - dx
    x= x1
    y=y1
    while(x<=x2):
        if (p < 0):
            xcoordinate.append(x)
            ycoordinate.append(y)
            x=x+1

            p = p + 2*dy
        else:
            xcoordinate.append(x)
            ycoordinate.append(y)
            x=x+1
            y+=1

            p = p + 2*dy -2*dx
         
    plt.plot(xcoordinate,ycoordinate,marker='*')
    plt.show()
bla()   



        




    
    

    