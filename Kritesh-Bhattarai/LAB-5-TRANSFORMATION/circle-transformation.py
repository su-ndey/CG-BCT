# midpoint method to draw a circle with transformations
import matplotlib.pyplot as plt
import numpy as np

# Input the radius and center of the circle
r = int(input("Enter the radius of the circle: "))
xc = int(input("Enter the x-coordinate of the center of the circle: "))
yc = int(input("Enter the y-coordinate of the center of the circle: "))

# Initialize variables
x = 0
y = r
p = 1 - r
xes = []
yes = []

# Function to plot the points of the circle
def plot_point(x, y, xc, yc):
    xes.extend([x + xc, -x + xc, x + xc, -x + xc, y + xc, -y + xc, y + xc, -y + xc])
    yes.extend([y + yc, y + yc, -y + yc, -y + yc, x + yc, x + yc, -x + yc, -x + yc])


plot_point(x, y, xc, yc)


while x < y:
    x += 1
    if p < 0:
        p = p + 2 * x + 1
    else:
        y -= 1
        p = p + 2 * (x - y) + 1
    plot_point(x, y, xc, yc)

# Apply transformations
def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

# Define transformation matrices
def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# Create composite transformation matrix
scale = scaling_matrix(2, 0.5)
translate = translation_matrix(50, 50)
rotate = rotation_matrix(np.pi / 6)
composite_matrix = np.dot(np.dot(rotate, scale), translate)

# Apply transformations to the circle points
xes_transformed, yes_transformed = apply_2d_transformation(np.array(xes), np.array(yes), composite_matrix)

plt.figure(figsize=(8, 8))
plt.scatter(xes, yes, marker='o', color='blue', label='Original Circle')
plt.scatter(xes_transformed, yes_transformed, marker='o', color='red', label='Transformed Circle')
plt.title("Midpoint Circle Drawing with Transformations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()