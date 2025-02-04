1.Initialize circle parameters: set x=0, y=r, and decision parameter p=1−r.

2.Generate circle points using Bresenham's algorithm by updating x, y, and p in a loop and storing the symmetric points of the circle in xes and yes.

3.Build a rotation transformation:
• Compute translation matrix to move center to origin.
• Define rotation matrix for angle θ.
• Compute inverse translation matrix to move center back.
• Multiply these matrices to form a composite matrix.

4.Convert xes and yes into homogeneous coordinates, then apply the composite rotation matrix.

5.Plot the original and rotated points using matplotlib.