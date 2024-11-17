import statistics
ratings = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
print("Frequency of each rating:")
for rating in range(1, 6):
    print(f"{rating}: {ratings.count(rating)}")
print("\nStatistics:")
print(f"Minimum: {min(ratings)}")
print(f"Maximum: {max(ratings)}")
print(f"Range: {max(ratings) - min(ratings)}")
print(f"Mean: {statistics.mean(ratings):.2f}")
print(f"Median: {statistics.median(ratings)}")
print(f"Mode: {statistics.mode(ratings)}")
print(f"Variance: {statistics.variance(ratings):.2f}")
print(f"Standard Deviation: {statistics.stdev(ratings):.2f}")
