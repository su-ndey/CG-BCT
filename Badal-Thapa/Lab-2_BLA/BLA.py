# BLA For All Cases
import matplotlib.pyplot as plt

def BLA():
    # Take user input for coordinates
    x1 = int(input("Enter the x1 coordinate: "))
    y1 = int(input("Enter the y1 coordinate: "))
    x2 = int(input("Enter the x2 coordinate: "))
    y2 = int(input("Enter the y2 coordinate: "))

    # Calculate differences and steps
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))  # Ensure steps is non-negative
    xincrement = dx / steps
    yincrement = dy / steps

    # Generate coordinates using list comprehensions
    x_coordinates = []
    y_coordinates = []

    for i in range(steps):
        x1=x1+xincrement
        y1=y1+yincrement
        x_coordinates.append(x1)
        y_coordinates.append(y1)

    # Plot the line
    plt.plot(x_coordinates, y_coordinates, marker='*')
    plt.show()

# Call the function
BLA()
