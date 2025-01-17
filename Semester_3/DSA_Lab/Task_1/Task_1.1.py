def postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '+':
                stack.append(num1 + num2)
            elif char == '-':
                stack.append(num1 - num2)
            elif char == '*':
                stack.append(num1 * num2)
            elif char == '/':
                stack.append(num1 / num2)
    return stack.pop()

user = input(f"\nEnter the postfix expression: ")
eval = postfix(user)
print(f"\nThe oput out of {user} = {eval}")
# input: 23+5*
# output: The output of 23+5* = 35
# input: 23*5+
# output: The output of 23*5+ = 11