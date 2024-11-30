import matplotlib.pyplot as plt
def dda():
    x1=int(input('Enter the value of x1'))
    y1=int(input('Enter the value of y1'))
    x2=int(input('Enter the value of x2'))
    y2=int(input('Enter the value of y2'))
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    xinc=dx/steps
    yinc=dy/steps
    xes=[x1]
    yes=[y1]

    for i in range(steps):
        xes.append(x1)
        yes.append(y1)
        x1=x1+xinc
        y1=y1+yinc
        print(f'{x1},{y1}')
    plt.plot(xes,yes,marker='*')
    plt.show()
dda()