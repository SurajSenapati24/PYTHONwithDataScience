# Data
personalities = [
    {"name": "Elon Musk", "net_worth": 433.9},
    {"name": "Jeff Bezos", "net_worth": 239.4},
    {"name": "Mark Zuckerberg", "net_worth": 211.8},
    {"name": "Larry Ellison", "net_worth": 204.6},
    {"name": "Bernard Arnault & Family", "net_worth": 181.3},
    {"name": "Larry Page", "net_worth": 161.4},
]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j]["net_worth"] < arr[min_idx]["net_worth"]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]["net_worth"] > arr[j + 1]["net_worth"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key["net_worth"] < arr[j]["net_worth"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

selection_sorted = personalities.copy()
bubble_sorted = personalities.copy()
insertion_sorted = personalities.copy()
selection_sort(selection_sorted)
bubble_sort(bubble_sorted)
insertion_sort(insertion_sorted)
def to_dict(sorted_list):
    return {item["name"]: item["net_worth"] for item in sorted_list}

selection_result = to_dict(selection_sorted)
bubble_result = to_dict(bubble_sorted)
insertion_result = to_dict(insertion_sorted)
print("Selection Sort Result:", selection_result)
print("Bubble Sort Result:", bubble_result)
print("Insertion Sort Result:", insertion_result)