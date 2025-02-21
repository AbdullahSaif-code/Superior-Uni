# Task 1: Code for LUHN Algorithm in Python

def luhn_algorithm(card_number):
    card_number = str(card_number)
    card_number = card_number[::-1]
    total = 0
    for i in range(len(card_number)):
        if i % 2 == 1:
            double = int(card_number[i]) * 2
            if double > 9:
                double = double - 9
            total += double
        else:
            total += int(card_number[i])
    return total % 10 == 0

print(luhn_algorithm(49927398716)) # True
print(luhn_algorithm(49927398717)) # False