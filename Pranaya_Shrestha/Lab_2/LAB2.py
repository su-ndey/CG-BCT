def BLA():

    x0=int(input("Enter value of x0: "))
    x1=int(input("Enter value of x1: "))
    y0=int(input("Enter value of y0: "))
    y1=int(input("Enter value of y1: "))

    del_x=abs(x1-x0)
    del_y=abs(y1-y0)

    sx=1 if x1>x0 else -1
    sy=1 if y1>y0 else -1

    if del_x>=del_y: ##For shallow slopes
        pk=2*del_y-del_x
    else: ##for steep slope
        pk=2*del_x-del_y


    x_coordinate=[x0]
    y_coordinate=[y0]
    x=x0
    y=y0
    for k in range (max(del_x,del_y)):
        if del_x>=del_y: ##for shallow slope

            x+=sx
            if pk>=0:
                y+=sy
                pk=pk+2*del_y-2*del_x
            
            else:
                pk=pk+2*del_y
            x_coordinate.append(x)
            y_coordinate.append(y)  
        else:
            y+=sy
            if pk>=0:
                x+=sx
                pk=pk+2*del_x-2*del_y

            else:
                pk=pk+2*del_x
            x_coordinate.append(x)
            y_coordinate.append(y)  
    import matplotlib.pyplot as plt

    plt.plot(x_coordinate,y_coordinate,marker="*")
    plt.show()

BLA()