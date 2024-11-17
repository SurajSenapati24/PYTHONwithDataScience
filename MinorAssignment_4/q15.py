import random

# Function to randomly fill a 4x4 matrix with 0s and 1s
def generate_matrix():
    matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
    return matrix

# Function to find the row with the most 1s
def find_row_with_most_ones(matrix):
    row_index = -1
    max_ones = -1
    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones:
            max_ones = ones_count
            row_index = i
    return row_index

# Function to find the column with the most 1s
def find_column_with_most_ones(matrix):
    column_index = -1
    max_ones = -1
    for j in range(4):
        ones_count = sum(1 for i in range(4) if matrix[i][j] == 1)
        if ones_count > max_ones:
            max_ones = ones_count
            column_index = j
    return column_index

# Main program
matrix = generate_matrix()

# Print the matrix
print("Matrix:")
for row in matrix:
    print("".join(map(str, row)))

# Find the row and column with the most 1s
largest_row_index = find_row_with_most_ones(matrix)
largest_column_index = find_column_with_most_ones(matrix)

# Display the results
print(f"The largest row index: {largest_row_index}")
print(f"The largest column index: {largest_column_index}")
