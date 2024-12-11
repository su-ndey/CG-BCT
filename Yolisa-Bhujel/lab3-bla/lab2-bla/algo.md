```markdown
# Midpoint Circle Algorithm Steps

### Step 1: Input Parameters
Enter the following parameters:
- **Radius (r)**: The radius of the circle.
- **Center Coordinates (xc, yc)**: The coordinates of the center of the circle.

### Step 2: Initialize Variables
- Set **x = 0** and **y = r**.
- Set the **initial decision parameter p = 1 - r**.

### Step 3: Plot Initial Points
Plot the initial points for **(x = 0, y = r)** and their symmetric counterparts in all 8 octants.

### Step 4: Loop and Update Points
Iterate while **x < y**:
- Increment **x** by 1.
- If **p < 0**:  
  Update **p = p + 2 * x + 1** (move horizontally).
- If **p ≥ 0**:  
  Decrease **y** by 1, and update **p = p + 2 * (x - y) + 1** (move diagonally).

### Step 5: Plot Points
After each update of **x** and **y**, plot the new points and their symmetric counterparts.

### Step 6: End
Stop once the loop ends (when **x ≥ y**) and display the complete circle using the plotted points.
```