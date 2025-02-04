# Midpoint Circle Drawing Algorithm

## Steps:

### 1. **Initialize Variables:**
   - Set `x = 0` and `y = r`.
   - Calculate the initial decision parameter: `p = 1 - r`.

### 2. **Define the plot_point Function:**
   - This function plots the eight symmetrical points for a given `(x, y)` around the center `(xc, yc)`:
     - `(x + xc, y + yc)`
     - `(-x + xc, y + yc)`
     - `(x + xc, -y + yc)`
     - `(-x + xc, -y + yc)`
     - `(y + xc, x + yc)`
     - `(-y + xc, x + yc)`
     - `(y + xc, -x + yc)`
     - `(-y + xc, -x + yc)`

### 3. **Initial Point Plot:**
   - Plot the points at `(0, r)` using the `plot_point` function.

### 4. **Loop to Draw the Circle:**
   - While `x < y`:
     1. Increment `x` by 1.
     2. If `p < 0`, update `p = p + 2x + 1` (no change to `y`).
     3. If `p >= 0`, decrement `y` by 1, and update `p = p + 2(x - y) + 1`.
     4. Plot the new points using the `plot_point` function.

### 5. **Plot the Circle:**
   - After the loop ends, plot all the points collected during the iteration.

### 6. **Display the Circle:**
   - Display the circle using a plotting library (e.g., `plt.show()`).