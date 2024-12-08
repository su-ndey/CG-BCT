#BLA for all cases

import matplotlib.pyplot as plt

def BLA():
    x1 = int(input('Enter the number x1:'))
    y1 = int(input('Enter the number y1:'))
    x2 = int(input('Enter the number x2:'))
    y2 = int(input('Enter the number y2:'))
    delx = abs(x2 - x1)
    dely = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    x_plot = [x1]
    y_plot = [y1]
    
    if delx > dely : 
        p = 2*dely - delx
        for i in range(max(x2, x1)-1):
            x1 = x1 + sx
            if p >= 0:
                y1 = y1 + sy
                p = p + 2*dely -2*delx
            else:
                p = p + 2*dely
            x_plot.append(x1)
            y_plot.append(y1)
            
    else: 
        p = 2*delx - dely
        for i in range(max(x2, x1)-1):
            y1 = y1 + sy
            if p >= 0:
                x1 = x1 + sx
                p = p + 2*delx -2*dely
            else:
                p = p + 2*delx
            x_plot.append(x1)
            y_plot.append(y1)

    plt.plot(x_plot, y_plot, marker = "*")
    plt.show()
BLA()
