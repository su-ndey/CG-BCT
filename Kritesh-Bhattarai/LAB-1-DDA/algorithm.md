# ALGORITHM FOR DDA
### Step 1:
Input the starting and ending points: (x1,y2) and (x2,y2)
### Step 2:
calculate the difference:
Δx= x2- x1 and Δy= y2-y1
### Step 3:
Determine the number of steps:
Steps = max(|Δx|,|Δy|)
### Step 4:
Calculate the increment:
Xincrement= Δx/steps  and yincrement = Δy/steps  
### Step 5:
Initialize starting point:
X= x1 and y=y1
### Step 6:
Iterate through the number of steps:
-Plot the point (x,y)
-Increment
    X= X+ Xincrement  y= y+yincrement
### Step 7:
Stop once all the steps are plotted