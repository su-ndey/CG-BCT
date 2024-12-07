import matplotlib.pyplot as plt

def midpoint():
    r = int(input("Enter Radius of Circle: "))
    Xc = int(input("Enter Center of Circle X-axis: "))
    Yc = int(input("Enter Center of Circle Y-axis: "))
    x, y = 0, r
    p = 1 - r
    Xes, Yes = [], []
    
    while x <= y:
        Xes.extend([x + Xc, y + Xc, -x + Xc, -y + Xc, -x + Xc, -y + Xc, x + Xc, y + Xc])
        Yes.extend([y + Yc, x + Yc, y + Yc, x + Yc, -y + Yc, -x + Yc, -y + Yc, -x + Yc])
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        x += 1
    plt.scatter(Xes, Yes, color="red", s=10)
    plt.grid()
    plt.show()

midpoint()
