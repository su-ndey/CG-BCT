# ALGORITHM FOR BRESENHAM
### Step 1:
#### Input starting and Ending Points.
### Step 2:
#### calculate the difference:
#### Δx= x2- x1 and Δy= y2-y1
### Step 3:
#### Determine the steps
### Step 4:
#### Initialize the starting points
### Step 5:
#### check conditions:
if dx > dy:
        p = 2 * dy - dx
        while x0 != x1:
            x0 = x0 + sx
            if p >= 0:
                y0 = y0 + sy
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            xes.append(x0)
            yes.append(y0)
    else:
        p = 2 * dx - dy
        while y0 != y1:
            y0 = y0 + sy
            if p >= 0:
                x0 = x0 + sx
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
            xes.append(x0)
            yes.append(y0)
### Step 6:
#### Plot the points
### Step 7:
#### stop.