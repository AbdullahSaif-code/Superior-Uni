# Insertion Sort Questions

# 1. Basic Insertion Sort Implementation:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_arr = [12, 11, 13, 5, 6]
print(insertion_sort(input_arr))

# 2. Insertion Sort for Linked Lists:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    sorted_head = ListNode(0)
    current = head

    while current:
        prev = sorted_head
        next_node = current.next

        while prev.next and prev.next.val < current.val:
            prev = prev.next

        current.next = prev.next
        prev.next = current
        current = next_node

    return sorted_head.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head = ListNode(12, ListNode(11, ListNode(13, ListNode(5, ListNode(6)))))
sorted_head = insertion_sort_linked_list(head)
print_linked_list(sorted_head)

# 3. Binary Insertion Sort Optimization:

def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i)
        arr.pop(i)
        arr.insert(j, key)
    return arr

print(binary_insertion_sort([12, 11, 13, 5, 6]))

# 4. Sort a List of Tuples Using Insertion Sort:

def insertion_sort_tuples(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[1] < arr[j][1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_tuples([(1, 3), (4, 1), (2, 2)]))

# 5. Insertion Sort with Reverse Sorting:

def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_descending([5, 2, 9, 1, 5, 6]))

# 6. Count Shifts During Insertion Sort:

def insertion_sort_count_shifts(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    print("Number of shifts:", shifts)
    return arr, shifts

print(insertion_sort_count_shifts([12, 11, 13, 5, 6]))

# 7. Insertion Sort in Matrix Sorting:

def insertion_sort_matrix(matrix):
    for row in matrix:
        for i in range(1, len(row)):
            key = row[i]
            j = i - 1
            while j >= 0 and key < row[j]:
                row[j + 1] = row[j]
                j -= 1
            row[j + 1] = key
    return matrix

matrix = [[5, 1, 4], [3, 9, 2], [8, 6, 7]]
print(insertion_sort_matrix(matrix))
