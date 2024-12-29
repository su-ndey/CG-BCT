import matplotlib.pyplot as plt
def scatter(xes,yes,x,y,xc,yc): 
    
    xes.extend([x+xc,-x+xc,-x+xc,x+xc,y+xc,-y+xc,y+xc,-y+xc])
    yes.extend([y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc])
    

def MCA():

    xc = int(input("enter the value of xc:"))       
    yc = int(input("enter the value of yc:"))
    r  = int(input("enter the radius:"))
   
    x=0
    y=r
    p = 1-r # Initial decision parameter
    
    xes = []
    yes = []
    
    scatter(xes,yes,x,y,xc,yc)
    
    while x < y:
        x = x+1 
        if p < 0:
            p = p + 2*x + 1

        else:
            y = y - 1
            p = p + 2*(x-y) + 1 

        scatter(xes,yes,x,y,xc,yc) 
    plt.title("Midpoint Algorithm of Circle ")
    plt.gca().set_aspect('equal',adjustable='box')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.scatter(xes,yes,marker='o')
    plt.grid(True)
    plt.show()

MCA()