import matplotlib.pyplot as plt

x0= int(input("enter the starting coordinate x0: "))
y0= int(input("enter the starting coordinate y0: "))
x1= int(input("enter the ending coordinate x1: "))
y1= int(input("enter the ending coordinate y1: "))

dx= abs(x1-x0)
dy= abs(y1-y0)
    
if (x1>x0):
    sx = 1
else:
    sx = -1
if ( y1 > y0 ):
    sy = 1
else:
    sy = -1
        
if ( dx >= dy ):
    print('the line has shallow slope(m<=1)')
    po = 2*dy - dx 
    
elif ( dx < dy ):
    print('the line has steep slope(m>1)')
    po = 2*dx - dy
pointsx=[]
pointsy=[]

for i in range(max(dx,dy)):   
    if ( dx >= dy ):
        x0 = x0 + sx
        if ( po >= 0 ):
            y0 = y0 + sy
            po = po + 2*dy - 2*dx
        else:
            po = po + 2*dy
        pointsx.append(x0)
        pointsy.append(y0)



    else:
        y0 = y0 + sy
        if ( po >= 0 ):
            x0 = x0 + sx
            po = po + 2*dx - 2*dy
        else:
            po = po + 2*dx
        pointsx.append(x0)
        pointsy.append(y0)


plt.plot(pointsx, pointsy, marker='.', color='teal')
plt.title("Bresenham's Line Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()