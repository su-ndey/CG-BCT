# midpoint method to draw a circle
import matplotlib.pyplot as plt

x = 0
r = int(input("Enter the radius of the circle: "))
xc = int(input("Enter the center of the circle: "))
yc = int(input("Enter the center of the circle: "))
y = r
p = 1 - r
xes = []
yes = []

def plot_point(x, y, xc, yc):
    xes.extend([x + xc, -x + xc, x + xc, -x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

plot_point(x, y, xc, yc)

while x < y:
    x += 1
    if p < 0:
        p = p + 2 * x + 1
    else:
        y -= 1
        p = p + 2 * (x - y) + 1
    plot_point(x, y, xc, yc)

plt.grid()
plt.scatter(xes, yes,marker='o', color='red')
plt.show()