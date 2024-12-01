import matplotlib.pyplot as plt

lx1 = []
ly2 = []
# putting number in list lx1
for i in range(2):
    a = int(input("Enter Number: "))
    lx1.append(a)
print(lx1)
# putting number in list ly2
for j in range(2):
    b = int(input("Enter Number: "))
    ly2.append(b)
print(ly2)

delta_x = ly2[0] - lx1[0]
delta_y = ly2[1] - lx1[1]
print(delta_x)
print(delta_y)

steps = max(abs(delta_x), abs(delta_y))
print(steps)

x_inc = delta_x / steps
y_inc = delta_y / steps

x = lx1[0]
y = ly2[1]

x_plot = [x]
y_plot = [y]

for i in range(steps):
    x = x + x_inc
    y = y + y_inc
    x_plot.append(x)
    y_plot.append(y)

print(x_plot)
print(y_plot)

plt.plot(x_plot, y_plot, marker = "*")
plt.show()