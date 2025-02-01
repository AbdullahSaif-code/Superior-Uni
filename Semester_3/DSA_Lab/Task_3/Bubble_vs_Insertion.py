
# Count and Compare Swaps in Bubble Sort vs Insertion Sort

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

def insertion_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        arr[j + 1] = key
        if j != i-1:
            swap_count += 1
    return swap_count

def compare_sorts(arr):
    arr_copy = arr.copy()
    bubble_swaps = bubble_sort(arr)
    insertion_swaps = insertion_sort(arr_copy)
    
    print(f"Bubble Sort swaps: {bubble_swaps}")
    print(f"Insertion Sort swaps: {insertion_swaps}")
    
    if bubble_swaps < insertion_swaps:
        print("Bubble Sort performs fewer swaps.")
    elif bubble_swaps > insertion_swaps:
        print("Insertion Sort performs fewer swaps.")
    else:
        print("Both sorting algorithms perform the same number of swaps.")

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
compare_sorts(arr)
