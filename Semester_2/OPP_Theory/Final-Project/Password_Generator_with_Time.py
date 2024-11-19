import random
import string
from datetime import datetime

# Base class (using inheritance and polymorphism)
class Main_Base:
    def __init__(self, length):
        self._length = length  # Private variable to store password length
        self._characters = string.digits  # Base characters (digits)

    # def generate_password(self):
    #     raise NotImplementedError("Subclass must implement this method.")

    # def _time_function(self):
    #     """Add time-based randomness, including year, month, day, hour, minute, second."""
    #     current_time = datetime.now()
        
    #     # Extract year, month, day, hour, minute, second
    #     year = current_time.year
    #     month = current_time.month
    #     day = current_time.day
    #     hour = current_time.hour
    #     minute = current_time.minute
    #     second = current_time.second

    #     # Use year, month, day, hour, minute, and second for randomness
    #     random_time = year + month + day + hour + minute + second
    #     random.seed(random_time)
    def _time_function(self):
        current_time = datetime.now()
        year = current_time.year
        month = current_time.month
        day = current_time.day
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        random_time = year + month + day + hour + minute + second
        random.seed(random_time)
        time_encryption = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        return time_encryption

    def generate_password(self):
        self._set_case_options()
        self._time_function()

        password = ''.join(random.choice(self._characters) for _ in range(self._length - 5))
        time_encryption = self._time_function()
        return password + time_encryption


# Encapsulation example specialized for simple passwords
class S_P_G(Main_Base):
    def __init__(self, length, Options):
        super().__init__(length)
        self.Options = Options

    def generate_password(self):
        self._set_case_options()
        self._time_function()

        # Generate simple password
        password = ''.join(random.choice(self._characters) for _ in range(self._length))
        return password

    def _set_case_options(self):
        # Encapsulated method to configure character options (lower, upper, or both)
        if self.Options == 'lower':
            self._characters += string.ascii_lowercase
        elif self.Options == 'upper':
            self._characters += string.ascii_uppercase
        elif self.Options == 'both':
            self._characters += string.ascii_letters

# Encapsulation + Inheritance example - specialized for complex passwords
class C_P_G(S_P_G):
    def __init__(self, length, Options, chars):
        super().__init__(length, Options)
        self.chars = chars

    def generate_password(self):
        super()._set_case_options()  # Use parent's case setting method
        if self.chars:
            self._characters += string.punctuation

        self._time_function()  # Add time-based randomness

        # Generate complex password
        password = ''.join(random.choice(self._characters) for _ in range(self._length))
        return password

# User input handling (encapsulation)
class Passwor_App:
    @staticmethod
    def user_input():
        # Get the length of the password
        while True:
            length = int(input("Enter length of password (at least 10): "))
            if length >= 10:
                break
            else:
                print("Try again! Password length is less than 10.")

        # Ask if the user wants to include special characters
        chars = input("Special characters? (yes/no): ").lower() == 'yes'

        # Ask for the case option: lower, upper, or both
        Options = ''
        while Options not in ['lower', 'upper', 'both']:
            Options = input("Options lowercase, uppercase, or both?\n(lower/upper/both): ").lower()

        return length, chars, Options

# Main function using polymorphism
def main():
    # Get inputs from the user
    length, chars, Options = Passwor_App.user_input()

    # Polymorphism: Choose generator based on special character option
    if chars:
        generator = C_P_G(length, Options, chars)
    else:
        generator = S_P_G(length, Options)

    # Generate and print the password
    password = generator.generate_password()
    print("Generated Password:", password)

# Run the main function
if __name__ == "__main__":
    main()
