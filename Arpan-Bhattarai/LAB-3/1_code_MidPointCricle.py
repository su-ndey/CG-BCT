import matplotlib.pyplot as plt

# Function to calculate and plot the symmetric points of the circle
def points_plot(xes, yes, x, y, xc, yc): 
    # Extend the x and y lists with 8 symmetric points for the current (x, y)
    xes.extend([x + xc, -x + xc, -x + xc, x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])

# Main function to implement the Midpoint Circle Algorithm
def MidPointCircle():
    # Taking radius and center coordinates as input from the user
    r = int(input("Enter the radius (r): "))
    xc = int(input("Enter the x-coordinate of the center (xc): "))       
    yc = int(input("Enter the y-coordinate of the center (yc): "))
   
    # Initializing variables
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter
    
    # Lists to store circle points
    xes = []
    yes = []
    
    # Plot the initial points
    points_plot(xes, yes, x, y, xc, yc)
    
    # Iterate while x is less than y
    while x < y:
        x = x + 1  # Increment x
        if p < 0:
            # If decision parameter is negative, update it for the next step
            p = p + 2 * x + 1
        else:
            # If decision parameter is non-negative, update y and the parameter
            y = y - 1
            p = p + 2 * (x - y) + 1 

        # Call function to add new points
        points_plot(xes, yes, x, y, xc, yc)
    
    # Plot all points
    plt.scatter(xes, yes, marker='o')  # Plot points as scatter plot
    plt.grid(True)  # Add grid to the plot
    plt.show()  # Display the plot

# Call the function to execute the algorithm
MidPointCircle()
