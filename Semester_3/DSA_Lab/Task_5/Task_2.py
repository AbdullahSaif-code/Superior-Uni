# Task 2: Custom Sort

words = ["apple", "banana", "kiwi", "grape", "cherry", "pear", "blueberry" ,'a','b']

def sort(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) > len(words[j]) or (len(words[i]) == len(words[j]) and words[i] > words[j]):
                words[i], words[j] = words[j], words[i]
    return words

sorted_words = sort(words)
print(sorted_words)