import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot the cube and rotation axis
def plot_cube(vertices, edges, axis_line=None, ax=None, title=""):
    """Plot cube and rotation axis"""
    # If no axes are provided, create a new figure and axes
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    
    # Plot vertices as blue points
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='blue')
    
    # Plot edges by connecting pairs of vertices
    for edge in edges:
        ax.plot([vertices[edge[0], 0], vertices[edge[1], 0]],
                [vertices[edge[0], 1], vertices[edge[1], 1]],
                [vertices[edge[0], 2], vertices[edge[1], 2]], 'b-')

    # If the axis of rotation is provided, plot it in red dashed line
    if axis_line is not None:
        ax.plot([axis_line[0], axis_line[3]],
                [axis_line[1], axis_line[4]],
                [axis_line[2], axis_line[5]], 'r--', linewidth=2, label='Rotation Axis')
    
    # Add labels, title, and a legend
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # Set equal aspect ratio for the axes
    ax.set_box_aspect([1, 1, 1])
    return ax

# Function to create a translation matrix
def translate_matrix(tx, ty, tz):
    """Create translation matrix"""
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

# Function to create a rotation matrix for rotation about the x-axis
def rotate_x_matrix(angle):
    """Create rotation matrix for x-axis in degrees"""
    angle = np.radians(angle)  # Convert angle to radians
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 1] # --no-warn-script-location
    ])

# Function to create a rotation matrix for rotation about the y-axis
def rotate_y_matrix(angle):
    """Create rotation matrix for y-axis in degrees"""
    angle = np.radians(angle)  # Convert angle to radians
    return np.array([
        [np.cos(angle), 0, np.sin(angle), 0],
        [0, 1, 0, 0],
        [-np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])

# Function to create a rotation matrix for rotation about the z-axis
def rotate_z_matrix(angle):
    """Create rotation matrix for z-axis in degrees"""
    angle = np.radians(angle)  # Convert angle to radians
    return np.array([
        [np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# Function to create a composite rotation matrix for arbitrary axis
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
    # Calculate direction of the rotation axis
    axis_direction = np.array([x2 - x1, y2 - y1, z2 - z1], dtype=np.float64)  # Ensure float type
    axis_norm = np.linalg.norm(axis_direction)  # Normalize the axis
    axis_direction /= axis_norm  # Perform division with no type conflict


    # 1. Translate to origin (move axis to the origin)
    T1 = translate_matrix(-x1, -y1, -z1)

    # 2. Rotate around the x-axis to align the axis with the zx-plane
    alpha = np.degrees(np.arctan2(axis_direction[1], axis_direction[2]))
    Rx = rotate_x_matrix(alpha)

    # 3. Rotate around the y-axis to align the axis with the z-axis
    beta = np.degrees(np.arctan2(axis_direction[0], axis_direction[2]))
    Ry = rotate_y_matrix(beta)

    # 4. Rotate about z-axis by the specified angle
    Rz = rotate_z_matrix(angle)

    # 5. Inverse transformations to undo the earlier translations and rotations
    Ry_inv = rotate_y_matrix(-beta)
    Rx_inv = rotate_x_matrix(-alpha)
    T2 = translate_matrix(x1, y1, z1)

    # Combine all the transformations into one composite rotation matrix
    composite = T2 @ Rx_inv @ Ry_inv @ Rz @ Ry @ Rx @ T1
    return composite

# Function to create the cube's vertices and edges
def create_cube():
    """Create vertices and edges of a cube"""
    vertices = np.array([
        [0, 0, 0, 1],  # Vertex 0
        [1, 0, 0, 1],  # Vertex 1
        [1, 1, 0, 1],  # Vertex 2
        [0, 1, 0, 1],  # Vertex 3
        [0, 0, 1, 1],  # Vertex 4
        [1, 0, 1, 1],  # Vertex 5
        [1, 1, 1, 1],  # Vertex 6
        [0, 1, 1, 1]   # Vertex 7
    ])
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom face
        [4, 5], [5, 6], [6, 7], [7, 4],  # Top face
        [0, 4], [1, 5], [2, 6], [3, 7]   # Vertical edges
    ]
    return vertices, edges

# Function to apply a transformation matrix to the cube's vertices
def transform_vertices(vertices, matrix):
    """Transform vertices using matrix multiplication"""
    return (matrix @ vertices.T).T

# Main function to run the program
def main():
    # Create the cube's vertices and edges
    vertices, edges = create_cube()

    # Define the rotation axis and angle
    x1, y1, z1 = 2, 1, 0  # First point of rotation axis
    x2, y2, z2 = 3, 3, 1  # Second point of rotation axis
    angle = 45  # Rotation angle in degrees

    # Get the composite transformation matrix for rotation
    composite = arbitrary_rotation_matrix(x1, y1, z1, x2, y2, z2, angle)

    # Apply the transformation to the cube's vertices
    transformed_vertices = transform_vertices(vertices, composite)
    print(transformed_vertices)

    # Visualization of the cube before and after transformation
    fig = plt.figure(figsize=(12, 5))

    # Plot the original cube
    ax1 = fig.add_subplot(121, projection='3d')
    plot_cube(vertices, edges, [x1, y1, z1, x2, y2, z2], ax1, "Original Cube")

    # Plot the rotated cube
    ax2 = fig.add_subplot(122, projection='3d')
    plot_cube(transformed_vertices, edges, [x1, y1, z1, x2, y2, z2], ax2, f"Rotated {angle}° around axis")

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
