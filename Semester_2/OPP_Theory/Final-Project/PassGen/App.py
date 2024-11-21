class Passwor_App:
    @staticmethod
    def user_input():
        while True:
            length = int(input("Enter length of password (at least 10): "))
            if length >= 10:
                break
            else:
                print("Password length is less than 10.")

        chars = input("Special characters? (yes/no): ").lower() == 'yes'
        
        Options = ''
        while Options not in ['lower', 'upper', 'both']:
            Options = input("Options lowercase, uppercase, or both?\n(lower/upper/both): ").lower()

        return length, chars, Options
