def quicksort(arr):
    def quicksort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_helper(low, pi - 1)
            quicksort_helper(pi + 1, high)

    def partition(low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j
    quicksort_helper(0, len(arr) - 1)

arr = [37, 2, 6, 4, 89, 8, 10, 12, 68, 45]
quicksort(arr)
print("Sorted array:", arr)