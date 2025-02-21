# Selection Sort Questions

# 1. Basic Selection Sort Implementation:

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([29, 10, 14, 37, 14]))

# 2. Sorting Strings Using Selection Sort:

def selection_sort_strings(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort_strings(["apple", "orange", "banana", "kiwi"]))

# 3. Descending Order Selection Sort:

def selection_sort_desc(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort_desc([12, 4, 45, 23, 18]))

# 4. Selection Sort with Custom Comparators:

def selection_sort_custom(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if len(arr[j]) > 1 and len(arr[min_index]) > 1:
                if arr[j][1] < arr[min_index][1]:
                    min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort_custom(["cat", "bat", "apple", "car"]))

# 5. Count the Number of Swaps:

def selection_sort_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, swaps

print(selection_sort_swaps([12, 4, 45, 23, 18]))