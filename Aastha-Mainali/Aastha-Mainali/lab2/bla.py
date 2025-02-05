#breshenhams line algorithm
import matplotlib.pyplot as plt
def lab2():
    x1=int(input('enter starting coordinates of the line'))
    y1=int(input('enter starting coordinates of the line'))
    x2=int(input('enter ending coordinates of the line'))
    y2=int(input('enter ending  coordinates of the line'))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p=2*dy-dx
    xes=[x1]
    yes=[y1]
    x=x1
    y=y1

    while(x<x2):
        if(p<0):
          x=x+1

          xes.append(x)
          yes.append(y)
          p=p+2*dy
        else:
          x=x+1
          y=y+1
          xes.append(x)
          yes.append(y)
          p=p+2*dy-2*dx
    print(xes)
    print(yes)
    plt.plot(xes,yes,marker='*')
    plt.show()
lab2()