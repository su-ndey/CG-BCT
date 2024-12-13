import matplotlib.pyplot as plt
def plot(xes,yes,x,y,xc,yc): # function define
    
    xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    


def MCA():

    r  = int(input("enter the radius:"))
    xc = int(input("enter the value of xc:"))       
    yc = int(input("enter the value of yc:"))
   
    x=0
    y=r
    p = 1-r # Initial decision parameter
    
    xes = []
    yes = []
    
    plot(xes,yes,x,y,xc,yc)
    
        

    while x < y:
        x = x+1 
        if p < 0:
            p = p + 2*x + 1

        else:
            y = y - 1
            p = p + 2*(x-y) + 1 

        plot(xes,yes,x,y,xc,yc)# calling plot function
    plt.title("Midpoint Circle Algorithm ")
    plt.gca().set_aspect('equal',adjustable='box')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.scatter(xes,yes,marker='o')# Plot each point after update
    plt.grid(True)
    plt.show()

MCA()   