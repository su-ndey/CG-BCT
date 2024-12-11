import matplotlib.pyplot as plt
def function_name():
    x1= int(input('Enter the number x1: '))
    y1 = int(input('Enter the nnumber y1: '))
    x2= int(input('Enter the number x2: '))
    y2 = int(input('Enter the nnumber y2: '))
    dx= x2-x1
    dy= y2-y1
    steps=max(abs(dx),abs(dy))
    xincrement= dx/steps
    yincrement= dy/steps
    x=x1
    y=y1
    x_coordinate=[]
    y_coordinate=[]
    for i in range(0,steps):
        x_coordinate.append(x1)
        y_coordinate.append(y1)
        x1=x1+xincrement
        y1=y1+yincrement
    print(f'The value of x_coordinate is {x_coordinate}')
    print(f'The value of y_coordinate is {y_coordinate}')

    plt.plot(x_coordinate,y_coordinate)
    plt.show()
function_name()
