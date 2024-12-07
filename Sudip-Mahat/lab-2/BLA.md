# Bresenham's Line Algorithm Steps

### Step 1: Input Points
Enter the starting point `(x₁, y₁)` and ending point `(x₂, y₂)`.

### Step 2: Calculate Differences
Compute:
- `Δx = |x₂ - x₁|`
- `Δy = |y₂ - y₁|`

### Step 3: Determine Steps
Choose the larger of `Δx` or `Δy` to decide the number of steps.

### Step 4: Initialize Variables
Set initial points `(x₁, y₁)` and step directions `(sx, sy)`.

### Step 5: Update Points
- If `Δx > Δy`:  
  Set `p = 2 * Δy - Δx`.  
  Increment `x₁`, and if `p ≥ 0`, increment `y₁`.

- If `Δy ≥ Δx`:  
  Set `p = 2 * Δx - Δy`.  
  Increment `y₁`, and if `p ≥ 0`, increment `x₁`.

### Step 6: Plot Points
Plot the generated points `(x₁, y₁)` on the graph.

### Step 7: End
Finish after plotting the line.