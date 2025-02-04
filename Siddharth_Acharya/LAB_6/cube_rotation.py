import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Taking Input From User
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
z1 = int(input('Enter z1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
z2 = int(input('Enter z2: '))
theta = np.radians(int(input('Enter angle to rotate: ')))

# Distance between points
v = abs(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)))

# Direction cosines
a = (x2 - x1) / v
b = (y2 - y1) / v
c = (z2 - z1) / v
d = math.sqrt((b * b) + (c * c))

# Rotation matrix values
sin_beta = a
cos_beta = d
sin_alpha = b / d
cos_alpha = c / d

# Transformation matrices
it = np.array([
    [1, 0, 0, x1],
    [0, 1, 0, y1],
    [0, 0, 1, z1],
    [0, 0, 0, 1]
])

irx = np.array([
    [1, 0, 0, 0],
    [0, cos_alpha, sin_alpha, 0],
    [0, -sin_alpha, cos_alpha, 0],
    [0, 0, 0, 1]
])

iry = np.array([
    [cos_beta, 0, sin_beta, 0],
    [0, 1, 0, 0],
    [-sin_beta, 0, cos_beta, 0],
    [0, 0, 0, 1]
])

rx = np.array([
    [1, 0, 0, 0],
    [0, cos_alpha, -sin_alpha, 0],
    [0, sin_alpha, cos_alpha, 0],
    [0, 0, 0, 1]
])

ry = np.array([
    [cos_beta, 0, -sin_beta, 0],
    [0, 1, 0, 0],
    [sin_beta, 0, cos_beta, 0],
    [0, 0, 0, 1]
])

rz = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta), np.cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

t = np.array([
    [1, 0, 0, -x1],
    [0, 1, 0, -y1],
    [0, 0, 1, -z1],
    [0, 0, 0, 1]
])

# Composite matrix
CM = it @ irx @ iry @ rz @ ry @ rx @ t

def create_cube():
    vertices = np.array([
        [0, 0, 0, 1], [1, 0, 0, 1],
        [1, 1, 0, 1], [0, 1, 0, 1],
        [0, 0, 1, 1], [1, 0, 1, 1],
        [1, 1, 1, 1], [0, 1, 1, 1]
    ])
    edges = np.array([
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ])
    return vertices, edges

vertices, edges = create_cube()

# Transformed coordinates
Transformed_coordinate = (CM @ vertices.T).T

def plot_cube(vertices, edges, axis_line=None, ax=None, title=""):
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='blue')

    for edge in edges:
        ax.plot(
            [vertices[edge[0], 0], vertices[edge[1], 0]],
            [vertices[edge[0], 1], vertices[edge[1], 1]],
            [vertices[edge[0], 2], vertices[edge[1], 2]],
            'b-'
        )

    if axis_line is not None:
        ax.plot(
            [axis_line[0], axis_line[3]],
            [axis_line[1], axis_line[4]],
            [axis_line[2], axis_line[5]],
            'r--',
            linewidth=2,
            label='Rotation Axis'
        )
        ax.legend()

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.set_box_aspect([1, 1, 1])
    return ax

# Visualization
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, projection='3d')
plot_cube(vertices, edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")
ax2 = fig.add_subplot(122, projection='3d')
plot_cube(Transformed_coordinate, edges, [x1, y1, z1, x2, y2, z2], ax2, f"Rotated {np.degrees(theta):.2f}° Around Axis")
plt.tight_layout()
plt.show()
