# Simple Dynamic Calculator
# Using PEMDAS ,BODMAS
# Parentheses , Excpresion , Multiplaction , Division , Adation , Subctration
def change_syomble(values):
        values = values.replace("X", "*").replace("x", "*").replace("^", "**")
        result = eval(values)
        return result
def main():
    print("Simple Dynamic Calculator")
    print("Enter a mathematical values (type 'Q' to quit).")
    while True:
        user_input = input("Values: ")
        if user_input.lower() == "Q":
            print("Exiting!")
            break
        else:
            print("Result:", change_syomble(user_input))
main()