def browser():
    back_stack = []
    forward_stack = []
    current = None
    while True:
        user = input(f"\nVisit the URL: ")
        if user == "exit":
            break
        elif user == "back":
            if back_stack:
                forward_stack.append(current)
                current = back_stack.pop()
        elif user == "forward":
            if forward_stack:
                back_stack.append(current)
                current = forward_stack.pop()
        else:
            back_stack.append(current)
            current = user
            forward_stack = []
        print(f"\nCurrent URL: {current}")
browser()
# input: www.google.com
# output: Current URL: www.google.com
# input: www.facebook.com
# output: Current URL: www.facebook.com
# input: back
# output: Current URL: www.google.com
# input: back
# output: Current URL: None
# input: forward
# output: Current URL: www.google.com
# input: exit
# output: exit program