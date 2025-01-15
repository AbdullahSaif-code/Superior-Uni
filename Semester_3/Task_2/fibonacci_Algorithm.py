# print(0)
# print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 9:
        newFibo = prev1 + prev2
        print(f"the number is: {newFibo}")
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)