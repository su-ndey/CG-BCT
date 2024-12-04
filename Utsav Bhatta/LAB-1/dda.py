import matplotlib.pyplot as plt
def dda():
    x1=int(input("enter the value of x1:"))
    y1=int(input("enter the value of y1:"))
    x2=int(input("enter the value of x2:"))
    y2=int(input("enter the value of y2:"))
    delx= x2-x1
    dely= y2-y1
    steps = max(abs(delx),abs(dely))
    xinc = (delx/steps)
    yinc = (dely/steps)
    x=x1
    y=y1
    x_cord=[]
    y_cord=[]

    for i in range (steps+1) :
        x += xinc  
        x_cord.append(x) 
        y += yinc
        y_cord.append(y)
    print(x_cord , y_cord) 
    plt.plot(x_cord,y_cord,marker="*")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(True)
    plt.title("dda")
    plt.show()
dda()