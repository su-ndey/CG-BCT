import matplotlib.pyplot as plt
def midpoint_ellipse(rx,ry,xc,yc):
    x=0
    y=ry
    xes=[]
    yes=[]
    rx2=rx*rx
    ry2=ry*ry

    p1= (ry**2) - ((rx**2)*ry) + (0.25*(rx**2)) #Initial decision paramater
    while 2*ry2*x <= 2*rx2*y:
    #Fun call for plot
        xes.extend([x+xc,-x+xc,x+xc,-x+xc])
        yes.extend([y+yc,y+yc,-y+yc,-y+yc])
        plt.scatter(xes,yes)
        # print({x},{y}) 
    #Update x and decision paramater
        if p1<0:
            x+=1
            p1+=2*ry**2*x+ry2
        else:
            x+=1
            y-=1
            p1+=2*ry2*x-2*rx^2*y+ry2

    p2=(ry**2*(x+0.5)**2) + (rx**2*(y-1)**2)- (rx**2*ry**2)
    while y>=0:
    #Fun call for plot
        xes.extend([x+xc,-x+xc,x+xc,-x+xc])
        yes.extend([y+yc,y+yc,-y+yc,-y+yc])
        # print({x},{y}) 
    
    #Update x and decision paramater
        if p2>0:
            y-=1
            p2-=2*rx**2*y+rx**2
        else:
            x+=1
            y-=1
            p2+=2*ry**2*x-2*rx2*y+ry**2


    plt.scatter(xes,yes, color='black',marker='o')

    plt.grid()

    plt.show()  
    # xc,yc=5,5
    # rx,ry=4,6 
rx=int(input("Enter the radiius along x-axis\n"))
ry=int(input("Enter the radiius along y-axis\n"))
xc=int(input("Enter the x-cord of the centre\n"))
yc=int(input("Enter the y-cord of the centre\n"))
midpoint_ellipse(rx,ry,xc,yc)