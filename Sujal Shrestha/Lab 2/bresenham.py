import matplotlib.pyplot as plt

x1=15
y1=8
x2=25
y2=14
diff_x = x2-x1
diff_y = y2-y1
x_coor=[]
y_coor=[]

if (x2>x1):
    sx= 1
else:
    sx= -1
if (y2>y1):
        sy=1
else:
        sy= -1
k=0
pk= 2*diff_y - diff_x
for i in range(max(diff_x, diff_y)):
        x_coor.append(x1)
        y_coor.append(y1)
        x1=x1+ sx
        if(pk>=0):
         y1=y1+sy
         pkk=pk+2*diff_y-2*diff_x
        else:
           pkk=pk+2*diff_y
        if (diff_x<diff_y):
                sx=1
        if (x2>x1):
                sx= 1
        else:
                sx= -1
        if (y2>y1):
                sy=1
        else:
                sy= -1
k=0
pk= 2*diff_x - diff_y
for i in range(max(diff_x, diff_y)):
        x_coor.append(x1)
        y_coor.append(y1)
        y1=y1+sy
        if(pk>=0):
           x1=x1+sx
           pkk=pk+2*diff_x-2*diff_y
        else:
          pkk=pk+2*diff_x

plt.plot(x_coor,y_coor,marker="*",color="red")    
plt.xlabel("x=axis")
plt.ylabel("y-axis")
plt.show()     
   
    







