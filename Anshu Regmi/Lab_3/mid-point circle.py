import matplotlib.pyplot as plt

def mid_point(x_center, y_center, r):
    x = 0
    y = r
    p = 1 - r
    
    # Lists to store points for plotting
    xes = []
    yes = []

    # Add initial points for circle symmetry
    def plot_points(x, y):
        xes.extend([x + x_center, -x + x_center, x + x_center, -x + x_center, 
                    y + x_center, -y + x_center, y + x_center, -y + x_center])
        yes.extend([y + y_center, y + y_center, -y + y_center, -y + y_center,
                    x + y_center, x + y_center, -x + y_center, -x + y_center])

    plot_points(x, y)

    # Midpoint circle algorithm loop
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        
        plot_points(x, y)

    # Plotting the circle
    plt.scatter(xes, yes, marker='o', color='blue')
    plt.grid(True)
    plt.axis('equal')  # To maintain aspect ratio
    plt.show()

# Taking user input
x_center = int(input("Enter x_c: "))
y_center = int(input("Enter y_c: "))
r = int(input("Enter r: "))

# Calling the mid_point function
mid_point(x_center, y_center, r)
