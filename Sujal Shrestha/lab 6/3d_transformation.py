import numpy as np  
import matplotlib.pyplot as plt
import math

# User inputs for rotation axis
x1 = int(input('Enter the value of x1: '))
y1 = int(input('Enter the value of y1: '))
z1 = int(input('Enter the value of z1: '))
x2 = int(input('Enter the value of x2: '))
y2 = int(input('Enter the value of y2: '))
z2 = int(input('Enter the value of z2: '))

def plot_cube(vertices, edges, axis_line=None, ax=None, title=""):
    """Plot cube and rotation axis."""
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    # Plot vertices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='blue')

    # Plot edges
    for edge in edges:
        ax.plot([vertices[edge[0], 0], vertices[edge[1], 0]],
                [vertices[edge[0], 1], vertices[edge[1], 1]],
                [vertices[edge[0], 2], vertices[edge[1], 2]], 'b-')

    # Plot rotation axis
    if axis_line is not None:
        ax.plot([axis_line[0], axis_line[3]],
                [axis_line[1], axis_line[4]],
                [axis_line[2], axis_line[5]], 'r--', linewidth=2, label='Rotation Axis')
        ax.legend()

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    return ax

# Translation matrices
TM = np.array([[1, 0, 0, -x1],
               [0, 1, 0, -y1],
               [0, 0, 1, -z1],
               [0, 0, 0, 1]])
T = np.array([[1, 0, 0, x1],
                [0, 1, 0, y1],
                [0, 0, 1, z1],
                [0, 0, 0, 1]])

# Rotation axis parameters
V = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))
a = (x2 - x1) / V
b = (y2 - y1) / V
c = (z2 - z1) / V
d = math.sqrt((b ** 2) + (c ** 2))

# Rotation matrices
def RxMatrix(V, a, b, c, d):
    return np.array([[1, 0, 0, 0],
                     [0, c / d, -b / d, 0],
                     [0, b / d, c / d, 0],
                     [0, 0, 0, 1]])

def RyMatrix(V, a, b, c, d):
    return np.array([[d, 0, -a, 0],
                     [0, 1, 0, 0],
                     [a, 0, d, 0],
                     [0, 0, 0, 1]])

def RzMatrix(theta):
    """Rotation about the Z-axis by angle theta (radians)."""
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta, cos_theta,  0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def IRxMatrix(V, a, b, c, d):
    return np.array([[1, 0, 0, 0],
                     [0, c / d, b / d, 0],
                     [0, -b / d, c / d, 0],
                     [0, 0, 0, 1]])

def IRyMatrix(V, a, b, c, d):
    return np.array([[d, 0, a, 0],
                     [0, 1, 0, 0],
                     [-a, 0, d, 0],
                     [0, 0, 0, 1]])

# Composite transformation matrix
theta = math.pi / 2  # 90 degrees in radians
composite = (
    T @
    IRxMatrix(V, a, b, c, d) @
    IRyMatrix(V, a, b, c, d) @
    RzMatrix(theta) @
    RyMatrix(V, a, b, c, d) @
    RxMatrix(V, a, b, c, d) @
    TM
)

print("Composite matrix is:\n", composite)

def create_cube():
    """Create cube vertices and edges."""
    vertices = np.array([
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ])
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]
    return vertices, edges

def transform_vertices(vertices, matrix):
    """Transform vertices using matrix multiplication."""
    print("Transformed matrix is:-",(matrix @ vertices.T).T)
    return (matrix @ vertices.T).T

def main():
    # Create cube
    vertices, edges = create_cube()

    # Transform vertices using the composite matrix
    transformed_vertices = transform_vertices(vertices, composite)

    # Visualization
    fig = plt.figure(figsize=(12, 5))

    # Original cube
    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(vertices[:, :3], edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")

    # Transformed cube
    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(transformed_vertices[:, :3], edges, [x1, y1, z1, x2, y2, z2], ax2, "Rotated Cube")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()