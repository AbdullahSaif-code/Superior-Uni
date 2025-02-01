# Implement Bubble Sort with Optimization

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f"Pass {i+1}: {arr}")
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
optimized_bubble_sort(arr)