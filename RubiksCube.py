import random
from enum import Enum

# Enum for six colors
class Color(Enum):
    COLOR1 = 1  
    COLOR2 = 2
    COLOR3 = 3
    COLOR4 = 4
    COLOR5 = 5
    COLOR6 = 6

class RubiksCube:
    # Initialize the cube with NxN size for each face and random colors.
    def __init__(self, N=3):
        self.N = N
        # Each face is represented as an NxN 2D list with random colors
        self.faces = {
            'F': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)],  # Front
            'B': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)],  # Back
            'L': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)],  # Left
            'R': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)],  # Right
            'U': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)],  # Up
            'D': [[random.choice(list(Color)) for _ in range(N)] for _ in range(N)]   # Down
        }

    def rotate_face_clockwise(self, face):
        # Rotate face 90 degrees clockwise.
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_counterclockwise(self, face):
        # Rotate face 90 degrees counterclockwise.
        for _ in range(3):  # 90° counterclockwise is equivalent to 3 clockwise rotations
            self.rotate_face_clockwise(face)

    def rotate_row(self, row, clockwise=True):
        # Rotate a row of the cube across the adjacent faces.
        if clockwise:
            # Rotating a row clockwise affects Left, Front, Right, Back faces
            self.faces['L'][row], self.faces['F'][row], self.faces['R'][row], self.faces['B'][row] = \
                self.faces['B'][row], self.faces['L'][row], self.faces['F'][row], self.faces['R'][row]
        else:
            # Counterclockwise rotation of a row
            self.faces['L'][row], self.faces['F'][row], self.faces['R'][row], self.faces['B'][row] = \
                self.faces['F'][row], self.faces['R'][row], self.faces['B'][row], self.faces['L'][row]

    def rotate_column(self, col, clockwise=True):
        # Rotate a column of the cube across adjacent faces.
        if clockwise:
            # Rotating a column clockwise affects Up, Front, Down, Back faces
            temp = [self.faces['U'][i][col] for i in range(self.N)]
            for i in range(self.N):
                self.faces['U'][i][col] = self.faces['B'][self.N-1-i][self.N-1-col]
                self.faces['B'][self.N-1-i][self.N-1-col] = self.faces['D'][self.N-1-i][col]
                self.faces['D'][self.N-1-i][col] = self.faces['F'][i][col]
                self.faces['F'][i][col] = temp[i]
        else:
            # Counterclockwise rotation of a column
            temp = [self.faces['U'][i][col] for i in range(self.N)]
            for i in range(self.N):
                self.faces['U'][i][col] = self.faces['F'][i][col]
                self.faces['F'][i][col] = self.faces['D'][self.N-1-i][col]
                self.faces['D'][self.N-1-i][col] = self.faces['B'][self.N-1-i][self.N-1-col]
                self.faces['B'][self.N-1-i][self.N-1-col] = temp[i]

    def random_rotate_face(self):
        # Randomly rotates a face either clockwise or counterclockwise.
        face = random.choice(['F', 'B', 'L', 'R', 'U', 'D'])
        clockwise = random.choice([True, False])
        self.rotate_cube(face, clockwise)

    def rotate_cube(self, face, clockwise=True):
        # Rotates an entire face and its adjacent faces.
        # First rotate the face itself
        if clockwise:
            self.rotate_face_clockwise(face)
        else:
            self.rotate_face_counterclockwise(face)
        
        # Now rotate the rows/columns on the adjacent faces (depends on the face)
        if face == 'F':
            self.rotate_row(self.N-1, clockwise)
        elif face == 'B':
            self.rotate_row(0, not clockwise)
        elif face == 'L':
            self.rotate_column(0, clockwise)
        elif face == 'R':
            self.rotate_column(self.N-1, not clockwise)
        elif face == 'U':
            self.rotate_row(0, not clockwise)
        elif face == 'D':
            self.rotate_row(self.N-1, clockwise)

    def print_cube(self):
        # Print the current state of the cube.
        for face, grid in self.faces.items():
            print(f"{face} face:")
            for row in grid:
                print(' '.join(color.name for color in row))
            print()

# Example
cube = RubiksCube(3)  # Create a 3x3 cube with random colors
cube.print_cube()      # Show the initial cube state

# Perform random rotations
print("\nPerforming random rotations...\n")
for _ in range(5):  # Perform 5 random rotations
    cube.random_rotate_face()

cube.print_cube()      # Show cube after random rotations
