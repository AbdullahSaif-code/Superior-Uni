# Sort text (word) in Alphabetical Order (without using sort function) can use ASCII

user_input = input("Enter a string: ")
user_input = user_input.lower()

def sort_text(string):
    words = string.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]
    return words
print(" ".join(sort_text(user_input)))