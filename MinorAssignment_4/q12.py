def column_sum(matrix, col_index):
    """Return the sum of all elements in a specified column."""
    return sum(row[col_index] for row in matrix)

# Predefined 3-by-4 matrix
matrix = [
    [1.5, 2, 3, 4],
    [5.5, 6, 7, 8],
    [9.5, 1, 3, 1]
]

# Display the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Display the sum of each column
print("\nSum of each column:")
for col in range(len(matrix[0])):
    print(f"Column {col + 1}: {column_sum(matrix, col):.2f}")
