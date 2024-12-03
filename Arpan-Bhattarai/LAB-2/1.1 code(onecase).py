import matplotlib.pyplot as plt



def bla():

    #Input the points

    x1 = int(input("Enter the value of x1: "))

    y1 = int(input("Enter the value of y1: "))

    x2 = int(input("Enter the value of x2: "))

    y2 = int(input("Enter the value of y2: "))

    

    # Calculate deltas

    dx = abs(x2 - x1)

    dy = abs(y2 - y1)



    #Decision parameter

    p = 2 * dy - dx



    #Initializing the lists to store the points

    xes = [x1]

    yes = [y1]



    x = x1

    y = y1



    while x != x2:

        if p < 0:

            x = x + 1

            p = p + 2 * dy

        else:

            x = x + 1

            y = y + 1

            p = p + 2 * dy - 2 * dx



        xes.append(x)

        yes.append(y)



    #Printing the points

    print("X coordinates:", xes)

    print("Y coordinates:", yes)



    # Plotting the points

    plt.plot(xes, yes, marker='o', color='blue')

    plt.show()



# Call the function

bla()