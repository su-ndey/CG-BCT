### Algorithm 

1. **Input:**
   - Start point \((x_0, y_0)\)
   - End point \((x_1, y_1)\)

2. **Bresenham's Line Algorithm (BLA):**
   - Compute differences:
     - \(\Delta x = |x_1 - x_0|\)
     - \(\Delta y = |y_1 - y_0|\)
   - Determine step directions:
     - \(s_x = 1\) if \(x_1 > x_0\), else \(s_x = -1\)
     - \(s_y = 1\) if \(y_1 > y_0\), else \(s_y = -1\)
   - Initialize coordinates:
     - Start at \((x_0, y_0)\)
   - Calculate initial decision parameter:
     - If \(\Delta x > \Delta y\): \(p = 2\Delta y - \Delta x\)
     - Else: \(p = 2\Delta x - \Delta y\)
   - Iterate over the dominant axis:
     - If \(\Delta x > \Delta y\), increment \(x\) at each step, adjusting \(y\) when \(p \geq 0\)
     - Otherwise, increment \(y\) at each step, adjusting \(x\) when \(p \geq 0\)
   - Append calculated coordinates to \([x_{\text{list}}, y_{\text{list}}]\)

3. **2D Transformation:**
   - Create transformation matrices:
     - **Scaling matrix**:  
       \[
       \begin{bmatrix} 
       2 & 0 & 0 \\ 
       0 & 0.5 & 0 \\ 
       0 & 0 & 1 
       \end{bmatrix}
       \]
     - **Translation to origin**:  
       \[
       \begin{bmatrix} 
       1 & 0 & -x_0 \\ 
       0 & 1 & -y_0 \\ 
       0 & 0 & 1 
       \end{bmatrix}
       \]
     - **Translation back**:  
       \[
       \begin{bmatrix} 
       1 & 0 & x_0 \\ 
       0 & 1 & y_0 \\ 
       0 & 0 & 1 
       \end{bmatrix}
       \]
   - Combine transformations into:
     \[
     T_{\text{composite}} = T_{\text{back}} \times T_{\text{scaling}} \times T_{\text{to origin}}
     \]

4. **Apply Transformation:**
   - Convert points \((x, y)\) into homogeneous coordinates \([x, y, 1]\)
   - Apply \(T_{\text{composite}}\) to transform the points.

5. **Plot:**
   - Plot the original line using the Bresenham points.
   - Plot the transformed line using the transformed coordinates.
   - Add titles, labels, and legend.

6. **Output:**
   - Display a graph with the original and transformed lines.
