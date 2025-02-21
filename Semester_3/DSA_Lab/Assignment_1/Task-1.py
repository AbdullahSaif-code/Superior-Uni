# Implementing a Stack using Python

class Stack:
    def __init__(self):
        self.stack = []
    def push(self):
        user = int(input("How many values u want to add: "))
        for i in range(user):
            item = input("Enter the value: ")
            self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop()
    def is_empety(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]

stack = Stack()
stack.push()   # Run push method to add values in stack 
stack.pop()    # Run pop method to remove values from stack
print(stack.is_empety())  # Check if stack is empty or not
print(stack.size())       # Check the size of stack
print(stack.peek())       # Check the top value of stack