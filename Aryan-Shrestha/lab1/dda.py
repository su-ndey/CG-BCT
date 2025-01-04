#DDA 

import matplotlib.pyplot as plt

def DDA():
    x1= int(input('Enter the number x1: '))
    y1 = int(input('Enter the nnumber y1: '))
    x2= int(input('Enter the number x2: '))
    y2 = int(input('Enter the nnumber y2: '))
    dx= abs(x2-x1)
    dy= abs(y2-y1)
    steps=max(dx,dy)
    xincrement= dx/steps
    yincrement= dy/steps
    x = min(x1, x2)
    y = min(y1, y2)
    xcordinate=[]
    ycordinate=[]
    for i in range(steps+1):
        xcordinate.append(x)
        ycordinate.append(y)        
        x=x+xincrement
        y=y+yincrement


    plt.plot(xcordinate,ycordinate,marker='o')
    plt.show()

DDA()   