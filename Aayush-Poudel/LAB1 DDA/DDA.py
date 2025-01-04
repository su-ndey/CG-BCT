import matplotlib.pyplot as plt

def dda():
    x1 = int(input('Enter the value of x1: '))
    y1 = int(input('Enter the value of y1: '))
    x2 = int(input('Enter the value of x2: '))
    y2 = int(input('Enter the value of y2: '))

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    xes = []
    yes = []
    x, y = x1, y1

    for i in range(steps):
        xes.append(x)
        yes.append(y)
        xi = dx / steps
        yi = dy / steps
        x = x + xi
        y = y + yi

    plt.plot(round(xes), round(yes), marker='x')
    plt.show()

dda()