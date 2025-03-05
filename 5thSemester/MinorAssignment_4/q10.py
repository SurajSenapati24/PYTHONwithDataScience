def sum_numeric_elements(tuples_of_tuples):
    """Calculates and prints the sum of all numeric elements in the inner tuples."""
    total_sum = 0
    for inner_tuple in tuples_of_tuples:
        for item in inner_tuple:
            if isinstance(item, (int, float)):
                total_sum += item
    print("Sum of all numeric elements:", total_sum)

# Example input
try:
    # Example tuple of tuples
    tuples_of_tuples = (
        (1, 2, 3),
        (4, "a", 6.5),
        (7, 8.9, "b"),
        (0,)
    )
    sum_numeric_elements(tuples_of_tuples)
except Exception as e:
    print("Error:", e)
