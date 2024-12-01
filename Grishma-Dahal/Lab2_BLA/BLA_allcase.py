import matplotlib.pyplot as plt

x1= int(input("enter the starting coordinate x1 : "))
y1= int(input("enter the starting coordinate y1 : "))
x2= int(input("enter the ending coordinate x2 : "))
y2= int(input("enter the ending coordinate y2 : "))

dx= abs(x2-x1)
dy= abs(y2-y1)

sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

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
        x1 = x1 + sx
        if ( po >= 0 ):
            y1 = y1 + sy
            po = po + 2*dy - 2*dx
        else:
            po = po + 2*dy
        pointsx.append(x1)
        pointsy.append(y1)
        print(f'({x1},{y1})')



    else:
        y1 = y1 + sy
        if ( po >= 0 ):
            x1 = x1 + sx
            po = po + 2*dx - 2*dy
        else:
            po = po + 2*dx
        pointsx.append(x1)
        pointsy.append(y1)
        print(f'({x1},{y1})')

plt.plot(pointsx, pointsy, marker='.', color='teal')
plt.title("Bresenham's Line Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
