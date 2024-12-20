Algorithm

1. Import `matplotlib.pyplot` as `plt`.
2. Take user input for starting and ending coordinates (`x1`, `y1`, `x2`, `y2`).
3. Initialize empty lists `xCord` and `yCord`.
4. Append starting coordinates to the lists (`x1` to `xCord`, `y1` to `yCord`).
5. Calculate `delta_x` and `delta_y` (differences between starting and ending coordinates).
6. Set the initial decision parameter `p = 2 * delta_y - delta_x`.
7. Loop while `x1 <= x2`:
   - Increment `x1` by 1.
   - Update `p` based on its value; if `p >= 0`, increment `y1` by 1.
   - Append updated `x1` and `y1` to the lists.
   - Print the coordinates.
8. Plot the points using `plt.plot()` with markers and display the plot using `plt.show()`.