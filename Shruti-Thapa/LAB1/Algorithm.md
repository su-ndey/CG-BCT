DDA 

1. Import `matplotlib.pyplot` as `pit`.
2. Take user input for starting and ending coordinates (`x1`, `x2`, `y1`, `y2`).
3. Calculate `del_x` and `del_y` as the differences between the coordinates.
4. Determine the number of steps: `steps = max(del_x, del_y)`.
5. Compute `x_increment` and `y_increment` based on the steps.
6. Initialize `x` and `y` with the starting coordinates and add them to their respective lists.
7. Loop for `steps` times:
   - Update `x` and `y` with increments.
   - Append the rounded values of `x` and `y` to their lists.
8. Print the x and y coordinate lists.
9. Plot the line using `matplotlib` and display it.