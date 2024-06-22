def print_spiral(n):
    # Initialize variables
    matrix = [[0] * n for _ in range(n)]
    num = 1
    x, y = n // 2, n // 2  # Starting position at the center

    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize direction index and steps for each direction
    direction_index = 0
    steps = 1

    # Fill the matrix in spiral order
    while num <= n * n:
        # Move in the current direction for the current steps
        dx, dy = directions[direction_index]
        for _ in range(steps):
            if 0 <= x < n and 0 <= y < n:
                matrix[x][y] = num
                num += 1
                x += dx
                y += dy

        # Change direction
        direction_index = (direction_index + 1) % 4

        # Increment steps every two directions
        if direction_index % 2 == 0:
            steps += 1

    # Print the matrix
    for row in matrix:
        for cell in row:
            print("{:3}".format(cell), end=" ")
        print()


# Set the size of the spiral
size = 5  # Change this to adjust the size of the spiral
print_spiral(size)


# def print_spiral(n):
#     # Initialize variables
#     matrix = [[0] * n for _ in range(n)]
#     num = 1
#     x, y = n // 2, n // 2  # Starting position at the center

#     # Move through each layer of the spiral
#     for d in range(n // 2 + 1):
#         # Move right
#         for _ in range(2 * d + 1):
#             if 0 <= x < n and 0 <= y < n:
#                 matrix[y][x] = num
#                 num += 1
#                 x += 1
#         # Move down
#         for _ in range(2 * d + 1):
#             if 0 <= x < n and 0 <= y < n:
#                 matrix[y][x] = num
#                 num += 1
#                 y += 1
#         # Move left
#         for _ in range(2 * d + 2):
#             if 0 <= x < n and 0 <= y < n:
#                 matrix[y][x] = num
#                 num += 1
#                 x -= 1
#         # Move up
#         for _ in range(2 * d + 2):
#             if 0 <= x < n and 0 <= y < n:
#                 matrix[y][x] = num
#                 num += 1
#                 y -= 1

#     # Print the matrix
#     for row in matrix:
#         for cell in row:
#             print("{:3}".format(cell), end=" ")
#         print()


# # Set the size of the spiral
# size = 5  # Change this to adjust the size of the spiral
# print_spiral(size)


def print_spiral2(n):
    # Initialize variables
    dx, dy = 1, 0
    x, y = 0, 0
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix with numbers from 1 to n^2
    for i in range(1, n*n + 1):
        matrix[y][x] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    # Print the matrix in spiral order
    for row in matrix:
        for num in row:
            print("{:2}".format(num), end=" ")
        print()


# Set the size of the spiral
size = 5  # Change this to adjust the size of the spiral
print_spiral2(size)
