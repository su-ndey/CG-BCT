import matplotlib.pyplot as plt
x1= int(input("enter the starting coordinate x1: "))
y1= int(input("enter the starting coordinate y1: "))
x2= int(input("enter the starting coordinate x2: "))
y2= int(input("enter the starting coordinate y2: "))

def Dda():
    dx= x2-x1
    dy= y2-y1
    steps= max(abs(dx),abs(dy))
    xin= dx/steps
    yin= dy/steps
    plotx= [x1]
    ploty= [y1]
    x=x1
    y=y1

    for i in range(steps):
        x= (x+xin)
        y= (y+yin)
        plotx.append(x)
        ploty.append(y)
        print(f'({x},{y})')
    plt.plot(plotx,ploty,marker='.',color='brown')
    plt.show()
Dda()