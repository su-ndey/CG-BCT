import matplotlib.pyplot as plt
x1= int (input ("enter the value of x1: "))
x2= int (input ("enter the value of x2: "))
y1= int (input ("enter the value of y1: "))
y2= int (input ("enter the value of y2: "))
diff_x=x2-x1
diff_y=y2-y1
steps=abs (diff_x) if abs (diff_x)>abs (diff_y) else abs(diff_y)
x_increment= diff_x/steps
y_increment= diff_y/steps
i=0
x_corrdinate=[]
y_corrdinate=[]
while i<steps:
    i+=1 
    x1=x1+(x_increment)
    y1=y1+(y_increment)
    x_corrdinate.append(round(x1))
    y_corrdinate.append(round(y1))
    print(f"({round(x1)},{round(y1)})")
plt.plot(x_corrdinate,y_corrdinate,marker="*",color="red",label="DDA LINE")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.title("DDA")
plt.legend()
plt.show()