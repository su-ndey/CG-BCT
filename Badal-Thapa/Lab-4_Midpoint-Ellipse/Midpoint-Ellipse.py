# Midpoint Ellipse Algorithm
# Date:- 2024-12-11
# By Badal Thapa
from matplotlib import pyplot as plt

def midpoint_ellipse(): 
    # input from the user
    X_c = int(input("Enter X-axis Center of Ellipse: ")) # ellipse center x-axis
    Y_c = int(input("Enter Y-axis Center of Ellipse: ")) # ellise center y-axis
    R_x = int(input("Enter X-axis radii of Ellipse: ")) # radii of ellipse x-axis major-axis
    R_y = int(input("Enter Y-axis radii of Ellipse: ")) # radii of ellipse y-axis minor-axis
    x, y = 0, R_y
    X_es = []
    Y_es = []

    # region 1 decision parameter
    P_1 = (R_y**2) - (R_x**2 * R_y) + 0.25 * (R_x**2)

    # iteration in region 1
    while (2 * (R_y**2) * x <= 2 * (R_x**2) * y):
        
        # add four symmetric points for the ellipse
        X_es.extend([x + X_c, -x + X_c, x + X_c, -x + X_c])
        Y_es.extend([y + Y_c, y + Y_c, -y + Y_c, -y + Y_c])
        # plt.scatter(X_es, Y_es, color='red', s=5)

        # udating x & decision parameter
        if P_1 < 0:
            x += 1
            P_1 += (2 * (R_y**2) * x + (R_y**2))
        else: 
            x += 1
            y -= 1
            P_1 += (2 * (R_y**2) * x - 2 * (R_x**2) * y + (R_y**2))
    
    # region 2 decision parameter:
    P_2 = ((R_y**2) * (x + 0.5)**2) + (R_x**2) * (y - 1)**2 - (R_x**2 * R_y**2)

    # iterate through region 2
    while y >= 0:
        # Add four symmetric points for the ellipse
        X_es.extend([x + X_c, -x + X_c, x + X_c, -x + X_c])
        Y_es.extend([y + Y_c, y + Y_c, -y + Y_c, -y + Y_c])
        # plt.scatter(X_es, Y_es, color='red', s=5)

        # updating y & decision parameter
        if (P_2 > 0):
            y -= 1
            P_2 -= (2 * (R_x**2) * y + (R_x**2))
        else: 
            x += 1
            y -= 1
            P_2 += (2 * (R_y**2) * x - 2 * (R_x**2) * y  + (R_x**2))            

    # Plotting the points
    plt.scatter(X_es, Y_es, color='red', s=5)  # Scatter plot with small points
    plt.grid(True)
    plt.title("Ellipse Using Midpoint Algorithm")
    # plt.axis('equal')  # Equal scaling on both axes for accurate ellipse shape
    plt.show()

# Calling the function to draw the ellipse
midpoint_ellipse()