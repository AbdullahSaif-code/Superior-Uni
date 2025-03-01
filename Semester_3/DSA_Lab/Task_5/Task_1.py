# Task 1: Sort the students by their grades
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 78),
    ("Eve", 92)
]
def sort_students(students):
# Implementing a simple bubble sort for demonstration
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j][1] < students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]
            elif students[j][1] == students[j+1][1] and j > 0:
                continue
    return students

sorted_students = sort_students(students)
print(sorted_students)