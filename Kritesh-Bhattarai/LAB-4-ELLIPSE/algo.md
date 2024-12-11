## Midpoint Ellipse Drawing Algorithm

### Purpose:
The algorithm is used to draw an ellipse using the midpoint ellipse drawing technique. The midpoint ellipse algorithm is based on decision parameters that help decide whether the next point should be placed in one of the octants of the ellipse.

### Steps:

1. **Initialize Variables:**
   - Let `rx` be the horizontal radius of the ellipse.
   - Let `ry` be the vertical radius of the ellipse.
   - Let `xc` be the x-coordinate of the center of the ellipse.
   - Let `yc` be the y-coordinate of the center of the ellipse.
   - Compute `rx2 = rx * rx` (square of the horizontal radius).
   - Compute `ry2 = ry * ry` (square of the vertical radius).
   - Compute `two_rx2 = 2 * rx2`.
   - Compute `two_ry2 = 2 * ry2`.

2. **First Region (Ellipse in the first octant):**
   - Initialize `x = 0` and `y = ry` (starting at the top of the ellipse).
   - Compute the initial decision parameter `p1 = ry2 - (rx2 * ry) + (0.25 * rx2)`.

3. **Plot points in the first region:**
   - While `two_ry2 * x <= two_rx2 * y` (i.e., while the ellipse is in the first region):
     - Plot the points in all four octants based on the symmetry of the ellipse:
       - Plot `(x + xc, y + yc)`, `(-x + xc, y + yc)`, `(x + xc, -y + yc)`, and `(-x + xc, -y + yc)`.
     - If `p1 < 0`, increment `x` by 1 and update `p1` as `p1 + two_ry2 * x + ry2`.
     - Otherwise, increment `x` by 1, decrement `y` by 1, and update `p1` as `p1 + two_ry2 * x - two_rx2 * y + ry2`.

4. **Second Region (Ellipse in the second octant):**
   - Initialize the decision parameter `p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)`.

5. **Plot points in the second region:**
   - While `y >= 0` (i.e., while the ellipse is still in the second region):
     - Plot the points in all four octants:
       - Plot `(x + xc, y + yc)`, `(-x + xc, y + yc)`, `(x + xc, -y + yc)`, and `(-x + xc, -y + yc)`.
     - If `p2 > 0`, decrement `y` by 1 and update `p2` as `p2 - two_rx2 * y + rx2`.
     - Otherwise, increment `x` by 1, decrement `y` by 1, and update `p2` as `p2 + two_ry2 * x - two_rx2 * y + rx2`.

6. **End:**
   - Once the loop ends, the entire ellipse is drawn.
   - Display the plot of the ellipse.

### Input:
- `rx`: Horizontal radius of the ellipse.
- `ry`: Vertical radius of the ellipse.
- `xc`: X-coordinate of the center of the ellipse.
- `yc`: Y-coordinate of the center of the ellipse.

### Output:
- A plot of the ellipse centered at `(xc, yc)` with radii `rx` and `ry`.
