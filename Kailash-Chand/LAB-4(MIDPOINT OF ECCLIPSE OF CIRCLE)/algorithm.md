# Midpoint Ellipse Drawing Algorithm

The Midpoint Ellipse Drawing algorithm is an efficient method for rasterizing an ellipse on a grid. It is based on decision parameters that help determine whether to move horizontally or vertically to approximate the ellipse. The algorithm ensures that the ellipse is symmetric in all quadrants.

## Steps of the Algorithm

1. **Input Parameters:**
   - `rx`: Radius of the ellipse along the x-axis (horizontal radius).
   - `ry`: Radius of the ellipse along the y-axis (vertical radius).
   - `xc`: X-coordinate of the center of the ellipse.
   - `yc`: Y-coordinate of the center of the ellipse.

2. **Initialization:**
   - Set `x = 0` (start at the center along the x-axis).
   - Set `y = ry` (start at the top of the ellipse along the y-axis).
   - Calculate `rx^2` and `ry^2` (squares of the radii).
   - Calculate `2 * rx^2` and `2 * ry^2` (used in the decision parameters).
   - Compute the initial decision parameter `p1` as:
     \[
     p1 = ry^2 - (rx^2 \times ry) + \frac{1}{4} \times rx^2
     \]
   
3. **First Region (ellipse has more horizontal elongation):**
   - Loop while `2 * ry^2 * x <= 2 * rx^2 * y`:
     - Plot the points in all four quadrants by reflecting the coordinates.
     - If `p1 < 0`, increment `x` and update `p1`:
       \[
       p1 = p1 + 2 \times ry^2 \times x + ry^2
       \]
     - If `p1 >= 0`, increment `x`, decrement `y`, and update `p1`:
       \[
       p1 = p1 + 2 \times ry^2 \times x - 2 \times rx^2 \times y + ry^2
       \]

4. **Second Region (ellipse has more vertical elongation):**
   - Compute the initial decision parameter `p2` as:
     \[
     p2 = ry^2 \times (x + 0.5)^2 + rx^2 \times (y - 1)^2 - rx^2 \times ry^2
     \]
   - Loop while `y >= 0`:
     - Plot the points in all four quadrants by reflecting the coordinates.
     - If `p2 > 0`, decrement `y` and update `p2`:
       \[
       p2 = p2 - 2 \times rx^2 \times y + rx^2
       \]
     - If `p2 <= 0`, increment `x`, decrement `y`, and update `p2`:
       \[
       p2 = p2 + 2 \times ry^2 \times x - 2 \times rx^2 \times y + rx^2
       \]

5. **End of Algorithm:**
   - The ellipse is drawn after these loops. The `plot` function is called to draw the ellipse for each calculated point.




