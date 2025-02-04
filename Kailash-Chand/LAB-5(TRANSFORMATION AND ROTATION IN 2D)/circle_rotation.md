### Algorithm for Drawing and Rotating a Circle Using Bresenham's Circle Algorithm

1. **Input:**
   - Radius \(r\)
   - Center of the circle \((x_c, y_c)\)
   - Rotation angle \(\theta\) (in radians)

2. **Bresenham's Circle Algorithm:**
   - Initialize:
     - \(x = 0\), \(y = r\)
     - Decision parameter: \(p = 1 - r\)
     - Empty lists `xes` and `yes` for storing circle points.
   - Define a function to plot the symmetric points of the circle:
     - For each calculated \((x, y)\), compute symmetric points:
       - \((x + x_c, y + y_c)\), \((-x + x_c, y + y_c)\), \((x + x_c, -y + y_c)\), \((-x + x_c, -y + y_c)\)
       - \((y + x_c, x + y_c)\), \((-y + x_c, x + y_c)\), \((y + x_c, -x + y_c)\), \((-y + x_c, -x + y_c)\)
     - Append the symmetric points to `xes` and `yes`.
   - Repeat until \(x < y\):
     - Increment \(x\).
     - Update \(p\):
       - If \(p < 0\): \(p = p + 2x + 1\)
       - Else:
         - Decrement \(y\): \(y = y - 1\)
         - \(p = p + 2(x - y) + 1\)
     - Plot the new points using the defined function.
   - Return `xes` and `yes` (circle points).

3. **2D Rotation:**
   - Define rotation matrix for angle \(\theta\):
     \[
     R = \begin{bmatrix}
     \cos\theta & -\sin\theta & 0 \\
     \sin\theta & \cos\theta & 0 \\
     0 & 0 & 1
     \end{bmatrix}
     \]
   - Define translation matrices:
     - **Translate to origin:**
       \[
       T_{\text{to origin}} = \begin{bmatrix}
       1 & 0 & -x_c \\
       0 & 1 & -y_c \\
       0 & 0 & 1
       \end{bmatrix}
       \]
     - **Translate back:**
       \[
       T_{\text{back}} = \begin{bmatrix}
       1 & 0 & x_c \\
       0 & 1 & y_c \\
       0 & 0 & 1
       \end{bmatrix}
       \]
   - Combine transformations:
     \[
     T_{\text{composite}} = T_{\text{back}} \times R \times T_{\text{to origin}}
     \]

4. **Apply Rotation:**
   - Convert circle points \((x, y)\) into homogeneous coordinates \([x, y, 1]\).
   - Apply \(T_{\text{composite}}\) to the points to get rotated coordinates.

5. **Plot:**
   - Plot the original circle points in blue.
   - Plot the rotated circle points in red.
   - Add a title, labels, and a grid for visualization.

6. **Output:**
   - Display a graph showing the original and rotated circles.

