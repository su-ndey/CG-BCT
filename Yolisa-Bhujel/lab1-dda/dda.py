import matplotlib.pyplot as plt
def DDA():
#input from user
    X1= int(input('enter first coordinate'))
    Y1= int(input('enter another coordinate'))
    X2= int(input('enter first coordinate'))
    Y2= int(input('enter another coordinate'))

    dx=X2-X1
    dy=Y2-Y1

    steps= max(abs(dx), abs(dy))
    X=[X1]
    Y=[Y1]
  
    xin= dx/steps
    yin=dy/steps 

    for i in range(steps):
     X1=X1+xin
     Y1=Y1+yin
     X.append(X1)
     Y.append(Y1)

    plt.plot(X, Y, marker='o')
    plt.show()





DDA()