#DDA 

import matplotlib.pyplot as plt

def DDA():
    x1= int(input('Enter the number x1: '))
    y1 = int(input('Enter the nnumber y1: '))
    x2= int(input('Enter the number x2: '))
    y2 = int(input('Enter the nnumber y2: '))
    dx= x2-x1
    dy= y2-y1
    steps=max(dx,dy)
    xincrement= dx/steps
    yincrement= dy/steps
    xcordinate=[]
    ycordinate=[]
    for i in range(steps):
        x1=x1+xincrement
        y1=y1+yincrement
        xcordinate.append(x1)
        ycordinate.append(y1)

    plt.plot(xcordinate,ycordinate,marker='o')
    plt.show()

DDA()        





