#mid point ellipse drawing algorithm
import matplotlib.pyplot as plt
def midpoint_ellipse(rx,ry,xc,yc):
    #initialize variable
    x=0
    y=ry
    
    xs=[]
    ys=[]
    
    #initial decision parameter for region 1
    p1= ry*ry-(rx*rx*ry)+(0.25*rx*rx)
    #iterate through region1
    while(2*ry*ry*x <= 2*rx*rx*y):
        #plot point for all four quadrants
         xs.append(x+xc)
         ys.append(y+yc)

         xs.append(-x+xc)
         ys.append(y+yc)

         xs.append(x+xc)
         ys.append(-y+yc)

         xs.append(-x+xc)
         ys.append(-y+yc)
         
         if(p1<0):
              x=x+1
              p1=p1+2*ry*ry*x+(ry*ry)
         else:
              x=x+1
              y=y-1
              p1=p1+2*ry*ry*x-2*rx*rx*y+(ry*ry)

    p2=(ry*ry*(x+0.5)*2)+(rx*rx(y-1)**2)-(rx*rx*ry*ry)

    while(y>=0):
        xs.append(x+xc)
        ys.append(y+yc)
        
        xs.append(-x+xc)
        ys.append(y+yc)


        xs.append(x+xc)
        ys.append(-y+yc)



        xs.append(-x+xc)
        ys.append(-y+yc)

        if(p2>0):
            y=y-1
            p2=p2-(2*rx*rx*y+rx*rx)
        else:
            x=x+1
            y=y-1
            p2=p2+2*ry*ry*x-2*rx*rx*y+(rx*rx)

                     
    plt.scatter(xs, ys, marker="o", color="blue")
    plt.title("Mid point ellipse algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

xc,yc=100,99
rx,ry=50,56
midpoint_ellipse(rx,ry,xc,yc)
     
     