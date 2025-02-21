# Insertion Algorithm in a Sorted List

def insert_in_sorted_list(sorted_list, element):
    sorted_list.append(element)
    i = len(sorted_list) - 2
    while i >= 0 and sorted_list[i] > element:
        sorted_list[i + 1] = sorted_list[i]
        i -= 1
    sorted_list[i + 1] = element
    return sorted_list
insert_in_sorted_list([10, 20, 30, 40, 50], 35)
# Output: [10, 20, 30, 35, 40, 50]