Algorithm for MCA (Midpoint Circle Algorithm)

1.Input:
 r: Radius of the circle.
 (xc,yc): Center coordinates of the circle.
 
2.Initialize:
 x = 0 (Initial x-coordinate).
 y = r (Initial y-coordinate).
 p = 1 - r 
 xes = [] 
 yes = []  

3.Plot Initial Points:
  Call the plot function to calculate and store the symmetric points of (x, y) with respect to the circle center (xc, yc).

4.Iterate While x < y:
   Increment x by 1.
   Check if the decision parameter p is less than 0:
   Update p = p + 2 * x + 1 (Move horizontally).
   Else:
  Decrement y by 1.
  Update p = p + 2 * (x - y) + 1 (Move diagonally).
  Call the plot function to calculate and store the symmetric points for the new (x, y).

5.Display Circle:
  Use matplotlib to plot the points stored in xes and yes as a scatter plot.
  Enable grid lines for better visibility.

6.End.