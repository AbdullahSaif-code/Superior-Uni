# Remove Punctuations from UserInput String (without using remove function)

def remove_punctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in string:
        if char not in punctuations:
            result += char
    return result
print(remove_punctuations("Hello! How are you?"))