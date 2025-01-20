Compute ∆x and ∆y, determine step directions (sx, sy).
Use Bresenham’s algorithm to generate (xes, yes).
Define a rotation matrix for the desired angle θ.
Create translation matrices to move the line center to the origin, apply rotation, then move back.
Combine these matrices into a single composite transformation matrix.
Convert (xes, yes) to homogeneous coordinates and multiply by the composite matrix.
Plot the original line and the transformed line.