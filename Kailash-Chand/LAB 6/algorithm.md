# 3D Cube Rotation Visualization

## Algorithm for 3D Transformation

1. **Input the 3D coordinates of the object**:
    - Read the vertices of the 3D object.

2. **Choose the type of transformation**:
    - Translation
    - Scaling
    - Rotation

3. **For Translation**:
    - Input the translation factors `Tx`, `Ty`, and `Tz`.
    - Apply the translation matrix:

      [1  0  0  Tx]
      [0  1  0  Ty]
      [0  0  1  Tz]
      [0  0  0  1 ]

    - Multiply the translation matrix with the coordinates of the object.

4. **For Scaling**:
    - Input the scaling factors `Sx`, `Sy`, and `Sz`.
    - Apply the scaling matrix:

      [Sx  0   0   0]
      [0   Sy  0   0]
      [0   0   Sz  0]
      [0   0   0   1]

    - Multiply the scaling matrix with the coordinates of the object.

5. **For Rotation**:
    - Choose the axis of rotation (X, Y, or Z).
    - Input the angle of rotation `θ`.
    - Apply the corresponding rotation matrix:
      - **Rotation about X-axis**:

         [1    0       0      0]
         [0  cosθ  -sinθ      0]
         [0  sinθ   cosθ      0]
         [0    0       0      1]

      - **Rotation about Y-axis**:

         [cosθ   0  sinθ    0]
         [0       1    0    0]
         [-sinθ  0  cosθ    0]
         [0       0    0    1]

      - **Rotation about Z-axis**:

         [cosθ  -sinθ      0  0]
         [sinθ   cosθ      0  0]
         [0         0      1  0]
         [0         0      0  1]

    - Multiply the rotation matrix with the coordinates of the object.

6. **Output the transformed coordinates**:
    - Display the new coordinates of the 3D object after transformation.

7. **End**