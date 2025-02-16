#3D TRANSFORMATION 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cube(vertices, edges, axis_line=None, ax=None, title=""):
    """Plot cube and rotation axis"""
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

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)

    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])
    return ax

def translate_matrix(tx, ty, tz):
    """Create translation matrix"""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def rotate_x_matrix(alpha):
    """Create rotation matrix for x-axis in degrees"""
    alpha = np.radians(alpha)  # Convert angle to radians
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(alpha), -np.sin(alpha), 0],
        [0, np.sin(alpha), np.cos(alpha), 0],
        [0, 0, 0, 1]
    ])

def rotate_y_matrix(beta):
    """Create rotation matrix for y-axis in degrees"""
    beta = np.radians(beta)
    return np.array([
        [np.cos(beta), 0, np.sin(beta), 0],
        [0, 1, 0, 0],
        [-np.sin(beta), 0, np.cos(beta), 0],
        [0, 0, 0, 1]
    ])

def rotate_z_matrix(theta):
    """Create rotation matrix for z-axis in degrees"""
    theta = np.radians(theta)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle):
    v = np.sqrt(pow((x2 - x1), 2) + pow((y2 - y1),2) + pow((z2 - z1),2))
    a = (x2 - x1)/v
    b = (y2 - y1)/v
    c = (z2 - z1)/v
    alpha = np.arcsin(b/np.sqrt(pow(b, 2) + pow(c, 2)))
    beta = np.arcsin(a/np.sqrt(pow(b, 2) + pow(c, 2)))
    # 1. Translation to origin
    T1 = translate_matrix(-x1, -y1, -z1)
    # 2. Rotation about x-axis to zx-plane
    Rx = rotate_x_matrix(alpha)
    # 3. Rotation about y-axis to z-axis
    Ry = rotate_y_matrix(beta)
    # 4. Rotation about z-axis by specified angle
    Rz = rotate_z_matrix(angle)
    # 5. Inverse transformations
    Ry_inv = rotate_y_matrix(-beta)
    Rx_inv = rotate_x_matrix(-alpha)
    T2 = translate_matrix(x1, y1, z1)
    # Calculate composite matrix using matrix multiplication
    composite = T1 @ Ry_inv @ Rx_inv @ Rz @ Ry @ Rx @ T2
    return composite

def create_cube():
    """Create vertices and edges of a cube"""
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
    """Transform vertices using matrix multiplication"""
    return (matrix @ vertices.T).T

def main():
    # Create cube
    vertices, edges = create_cube()

    # Define rotation axis and angle
    x1, y1, z1 = 0, 0, 0  #  first point of axis
    x2, y2, z2 = 1, 0, 1  #  second point of axis
    angle = 45  #  angle in degrees
     # Get composite transformation matrix
    composite = arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle)

    # Transform vertices using matrix multiplication
    transformed_vertices = transform_vertices(vertices, composite)

    # Visualization
    fig = plt.figure(figsize=(12, 5))

    # Original cube
    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(vertices, edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")

    # Transformed cube
    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(transformed_vertices, edges, [x1, y1, z1, x2, y2, z2], ax2,f"Rotated {angle}° around axis")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()