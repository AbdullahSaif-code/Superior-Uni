# Reverse a String Using a Stack

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
Stack = Stack()
def reverse_string(input_string):
    for char in input_string:
        Stack.push(char)
    
    reversed_string = ''
    while not Stack.isEmpty():
        reversed_string += Stack.pop()
    return reversed_string

input_string = "Hello, World!"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))