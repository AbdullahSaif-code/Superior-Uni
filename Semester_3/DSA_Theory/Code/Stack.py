# Stack pverview
# use an opbject

class stack:
    def __init__(self, stack_len):
        self.stack1 = []
        self.limit = stack_len
    def push (self):
        if len(self.stack1) == self.limit:
            print("Stack is full.")
        else:
            print(f"Stack have vlaue of {len(self.stack1)}")
            for i in range(self.limit - len(self.stack1)):
                user_input = input("Enter Value: ")
                self.stack1.append(user_input)
                print(f"updated Stack: {self.stack1}")
    def display(self):
        if not self.stack1:
            print(f"Stack is Empety")
        else:
            print(f"Stack Values\n{self.stack1}")

user_limit = int(input("Enter length of Stack: "))
obj1 = stack(user_limit)
obj1.push()

def main():
    print(f"1.Enter Values\n2.Remove Value\n3.Exit")
    user_input = input("Enter opreation option: ")