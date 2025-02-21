# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Performance Comparison
import time
import random

arr = [64, 34, 25, 12, 22, 11, 90]
start_time = time.time()
bubble_sort(arr)
print("Bubble Sort Time: %s seconds" % (time.time() - start_time))
selection_sort(arr)
print("Selection Sort Time: %s seconds" % (time.time() - start_time))
insertion_sort(arr)
print("Insertion Sort Time: %s seconds" % (time.time() - start_time))