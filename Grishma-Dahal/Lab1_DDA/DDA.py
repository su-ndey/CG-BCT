import matplotlib.pyplot as plt

def DDA():
  #input from user
    x1= int(input('enter the first coordinate'))  
    y1= int(input('enter another coordinate'))
    x2= int(input('enter the first coordinate'))
    y2= int(input('enter another coordinate'))
    # x1= 1  
    # y1= 2
    # x2= 3
    # y2= 4
    dx= x2-x1
    dy= y2-y1
    steps= max(abs(dx),abs(dy))
    xes=[x1]
    yes=[y1]
    xincrement=dx/steps
    yincrement=dy/steps
    for i in range(steps):
        x1=x1+xincrement
        y1=y1+yincrement
        xes.append(x1)
        yes.append(y1)
    plt.plot(xes,yes,marker='o')
    plt.show()
   
DDA()
   
   
  

    
