import matplotlib.pyplot as plt

def BLA():
    x1=int(input('enter the first coordinate :  '))
    y1=int(input('enter the second coordinate :  '))
    x2=int(input('enter the end coordinate :  '))
    y2=int(input('enter the end coordinate :  '))

    dx = abs(x2-x1)
    dy = abs(y2-y1)

    x= 1 if x2 > x1 else -1
    y = 1 if y2 > y1 else -1

    x_plot =[x1]
    y_plot = [y1]

    if dx > dy:
        p = 2*dy - dx
        for i in range(max(x2 , x1)-1):
            x1=x1+x
            if p >= 0:
                y1=y1 + y
                p = p+2*dy-2*dx
            else:
                p=p+2*dy

            x_plot.append(x1)
            y_plot.append(y1)
    else:
                p=2*dx-dy
    for i in range(max(x2,x1)-1):
         y1=y1+y
         if p >= 0:
              x1=x1+x
              p=p+2*dx-2*dy
         else:
              p=p+2*dx
              x_plot.append(x1)
              y_plot.append(y1)
    plt.title("BLA line plot")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x_plot , y_plot, marker = "o")
    plt.show()

BLA()              


              


         
         









