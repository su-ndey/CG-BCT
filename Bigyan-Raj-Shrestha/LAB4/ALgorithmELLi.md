
1. **Input Parameters**:
   - The user provides the radii `rx` (x-axis) and `ry` (y-axis), and the center coordinates `xc` (x-coordinate) and `yc` (y-coordinate) of the ellipse.

2. **Initialization**:
   - Set initial values: `x = 0`, `y = ry` (starting point in the first quadrant).
   - Calculate `rx2 = rx^2` and `ry2 = ry^2`.
   - Initialize the first decision parameter `p1` using the formula:
     \[
     p1 = ry^2 - rx^2 \cdot ry + \frac{1}{4} \cdot rx^2
     \]

3. **First Region Calculation (x ≤ y)**:
   - Iterate while \( 2 \cdot ry^2 \cdot x \leq 2 \cdot rx^2 \cdot y \) (first region of the ellipse).
   - For each point `(x, y)`, calculate and store four symmetric points in all quadrants.
   - Update `x` and decision parameter `p1` based on its value:
     - If `p1 < 0`: Increment `x`.
     - If `p1 ≥ 0`: Increment `x` and decrement `y`.

4. **Second Region Calculation (x > y)**:
   - Calculate the second decision parameter `p2`:
     \[
     p2 = ry^2 \cdot (x + 0.5)^2 + rx^2 \cdot (y - 1)^2 - rx^2 \cdot ry^2
     \]
   - Iterate while `y ≥ 0` (second region of the ellipse).
   - For each point `(x, y)`, calculate and store four symmetric points in all quadrants.
   - Update `y` and decision parameter `p2` based on its value:
     - If `p2 > 0`: Decrement `y`.
     - If `p2 ≤ 0`: Increment `x` and decrement `y`.

5. **Plotting**:
   - Use `plt.scatter()` to plot all calculated points from both regions.

6. **Display**:
   - Add gridlines with `plt.grid()`.
   - Display the plot with `plt.show()`.

7. **User Interaction**:
   - User inputs the ellipse parameters, and the function generates and plots the ellipse on the graph.