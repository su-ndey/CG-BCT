Input --> r, center(Xc, Yc) // Where Xc & Yc is center of circle
x = 0, y = r // Where r is radius
points(p) = 1 - r
list of octanes Xes = [], Yes = []
Append first point (0, r) to the respective list
& call symmetry function
While x < y:
x += 1
if p < 0:
p += 2x + 1
if p >= 0:
y += 1
p += 2(x-y)+1
call symmetry function

symmetric point plotting function:
append(x + Xc, y + Yc)
append([
-x, y
-x, -y
x, -y
y, x
-y, x
y, -x
-y, -x
])