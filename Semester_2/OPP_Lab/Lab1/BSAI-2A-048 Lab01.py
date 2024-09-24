def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
while True:
    num = int(input("Enter number to check: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")