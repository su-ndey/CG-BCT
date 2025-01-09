import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot the cube and rotation axis
def plot_cube(vertices, edges, axis_line=None, ax=None, title=""):
    """Plot cube and rotation axis"""
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='blue')
    
    for edge in edges:
        ax.plot([vertices[edge[0], 0], vertices[edge[1], 0]],
                [vertices[edge[0], 1], vertices[edge[1], 1]],
                [vertices[edge[0], 2], vertices[edge[1], 2]], 'b-')

    if axis_line is not None:
        ax.plot([axis_line[0], axis_line[3]],
                [axis_line[1], axis_line[4]],
                [axis_line[2], axis_line[5]], 'r--', linewidth=2, label='Rotation Axis')
    
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    ax.set_box_aspect([1, 1, 1])
    return ax

def translate_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def rotate_x_matrix(angle):
    angle = np.radians(angle)
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1]
    ])

def rotate_y_matrix(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])

def rotate_z_matrix(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle):
    """
    Create composite matrix for rotation about arbitrary axis
    Steps:
    1. Translate to origin
    2. Rotate about x-axis to zx-plane
    3. Rotate about y-axis to z-axis
    4. Rotate about z-axis by angle
    5. Inverse transformations
    """

    # 1. Translate to origin (move axis to the origin)
    T1 = translate_matrix(-x1, -y1, -z1)

    # 2. Calculate the rotation angles for x and y axes
    alpha = np.degrees(np.arctan2(y2 - y1, z2 - z1))  # Rotation around X-axis
    beta = np.degrees(np.arctan2(x2 - x1, z2 - z1))   # Rotation around Y-axis

    # 3. Rotate around the x-axis to align the axis with the zx-plane
    Rx = rotate_x_matrix(alpha)

    # 4. Rotate around the y-axis to align the axis with the z-axis
    Ry = rotate_y_matrix(beta)

    # 5. Rotate about z-axis by the specified angle
    Rz = rotate_z_matrix(angle)

    # 6. Inverse transformations to undo the earlier translations and rotations
    Ry_inv = rotate_y_matrix(-beta)
    Rx_inv = rotate_x_matrix(-alpha)
    T2 = translate_matrix(x1, y1, z1)

    # Combine all the transformations into one composite rotation matrix
    composite = T2 @ Rx_inv @ Ry_inv @ Rz @ Ry @ Rx @ T1
    return composite

def create_cube():
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
    return (matrix @ vertices.T).T

def main():
    vertices, edges = create_cube()

    # Rotation axis defined by two points
    x1, y1, z1 = 2, 1, 0  # First point of rotation axis
    x2, y2, z2 = 3, 3, 1  # Second point of rotation axis
    angle = 90  # Rotation angle in degrees

    # Get the composite transformation matrix for rotation
    composite = arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle)

    # Apply the transformation to the cube's vertices
    transformed_vertices = transform_vertices(vertices, composite)

    # Visualization of the cube before and after transformation
    fig = plt.figure(figsize=(12, 5))

    # Plot the original cube
    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(vertices, edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")

    # Plot the rotated cube
    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(transformed_vertices, edges, [x1, y1, z1, x2, y2, z2], ax2, f"Rotated {angle}° around axis")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
