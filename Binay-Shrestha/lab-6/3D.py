import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    """Create a translation matrix"""
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])

def rotate_x_matrix(angle):
    """Create a rotation matrix for the x-axis in degrees"""
    return np.array([[1, 0, 0, 0],
                     [0, np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
                     [0, np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
                     [0, 0, 0, 1]])

def rotate_y_matrix(angle):
    """Create a rotation matrix for the y-axis in degrees"""
    return np.array([[np.cos(np.radians(angle)), 0, np.sin(np.radians(angle)), 0],
                     [0, 1, 0, 0],
                     [-np.sin(np.radians(angle)), 0, np.cos(np.radians(angle)), 0],
                     [0, 0, 0, 1]])

def rotate_z_matrix(angle):
    """Create a rotation matrix for the z-axis in degrees"""
    return np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0, 0],
                     [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle):
    """Create composite matrix for rotation about arbitrary axis"""
    v = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    a = (x2 - x1) / v
    b = (y2 - y1) / v
    c = (z2 - z1) / v

    alpha = np.arctan2(b, c)
    beta = np.arcsin(a)

    T1 = translate_matrix(-x1, -y1, -z1)
    Rx = rotate_x_matrix(np.degrees(-alpha))
    Ry = rotate_y_matrix(np.degrees(-beta))
    Rz = rotate_z_matrix(angle)
    Ry_inv = rotate_y_matrix(np.degrees(beta))
    Rx_inv = rotate_x_matrix(np.degrees(alpha))
    T2 = translate_matrix(x1, y1, z1)

    return T2 @ Rx_inv @ Ry_inv @ Rz @ Ry @ Rx @ T1

def create_cube():
    """Create vertices and edges for a cube"""
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
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    return vertices, edges

def transform_vertices(vertices, matrix):
    """Transform vertices using matrix multiplication"""
    return (matrix @ vertices.T).T




def main():
    """Main function"""
    vertices, edges = create_cube()

    x1, y1, z1 = 2, 1, 0
    x2, y2, z2 = 3, 3, 1
    angle = 90 # in degrees

    composite_matrix = arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle)

    transformed_vertices = transform_vertices(vertices, composite_matrix)
    print(transformed_vertices)
    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(vertices[:, :3], edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")

    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(transformed_vertices[:, :3], edges, [x1, y1, z1, x2, y2, z2], ax2, f"Rotated {angle}° around axis")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
