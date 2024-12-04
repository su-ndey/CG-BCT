import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    delx = abs(x2-x1)
    dely = abs(y2-y1)
    m = dely / delx if delx != 0 else float('inf')
    
    x,y=x1,y1
    xcord = []
    ycord = []

    P=2*dely-delx
    
    if m<=1:
        while x<=x2:
            xcord.append(x)
            ycord.append(y)
            
            if P<0:
                P+=2*dely
            else:
                P+=2*(dely-delx)
                y+=1
            
            x+=1

    else:
        P=2*delx-dely
        while y <= y2:
            xcord.append(x)
            ycord.append(y)
            
            if P<0:
                P+=2*delx
            else:
                P+=2*(delx-dely)
                x+=1
            
            y += 1

    return xcord,ycord

x1 = int(input("Enter the x-coordinate of the start point (x1): "))
y1 = int(input("Enter the y-coordinate of the start point (y1): "))
x2 = int(input("Enter the x-coordinate of the end point (x2): "))
y2 = int(input("Enter the y-coordinate of the end point (y2): "))

xcord,ycord=bresenham(x1,y1,x2,y2)

plt.figure(figsize=(8,8))
plt.plot(xcord, ycord, marker='o', color='b', label="Bresenham's Line")
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()