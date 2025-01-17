def stack():
    stack = []
    string = input(f"\nEnter a string: ")
    reversed_string = ""
    for i in string:
        stack.append(i)
    while stack:
        reversed_string += stack.pop() 
    if string == reversed_string:
        print(f"{string} is a palindrome.")
    else: 
        print(f"{string} is not a palindrome.")
while True:
    stack()
# input: madam
# output: madam is a palindrome.
# input: hello
# output: hello is not a palindrome.