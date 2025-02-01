
# Balanced Parentheses Checker Using a Stack
def is_balanced_parentheses(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if stack == [] or matching_parentheses[char] != stack.pop():
                return False
    return stack == []

# Example usage:
input_string = "{[()]}"
print(is_balanced_parentheses(input_string))  # Output: True

input_string = "{[(])}"
print(is_balanced_parentheses(input_string))  # Output: False
