import matplotlib.pyplot as plt

def MCA():
    def SP(x,y):
        xes.append(x)
        yes.append(y)
        xes.extend([x, -x, -x, x, y, -y, -y, y])
        yes.extend([y, y, -y, -y, x, x, -x, -x])
    
    r=int(input('Enter the radius: '))
    xc=int(input('Enter the x coord of center: '))
    yc=int(input('Enter the y coord of center: '))
    x,y=0,r
    p=1-r
    xes=[]
    yes=[]
    SP(x,y)
    while(x<y):
        x=x+1
        if(p<0):
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*(x-y)+1
        SP(x,y)
    
    xes = [xc + xi for xi in xes]
    yes = [yc + yi for yi in yes]
    plt.scatter(xes, yes, color='blue', s=10)
    plt.title("Midpoint Circle Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()
MCA()

        
