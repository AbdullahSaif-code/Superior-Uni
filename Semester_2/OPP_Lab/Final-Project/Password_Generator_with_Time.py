import random
import string
from datetime import datetime

# Base class (using inheritance and polymorphism)
class Main_Base:
    def __init__(self, length):
        self._length = length  # Private variable to store password length
        self._characters = string.digits  # Base characters (digits)

    def generate_password(self):
        """Generate a password. To be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement this method.")

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


# Encapsulation example - specialized for simple passwords
class Simple_Password_Gen(Main_Base):
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
class Complex_Password_Gen(Simple_Password_Gen):
    def __init__(self, length, Options, special_chars):
        super().__init__(length, Options)
        self.special_chars = special_chars

    def generate_password(self):
        super()._set_case_options()  # Use parent's case setting method
        if self.special_chars:
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
            length = int(input("Enter the desired length of the password (at least 10): "))
            if length >= 10:
                break
            else:
                print("Password length must be at least 5. Try again!")

        # Ask if the user wants to include special characters
        special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        # Ask for the case option: lower, upper, or both
        Options = ''
        while Options not in ['lower', 'upper', 'both']:
            Options = input("Should the password have lowercase, uppercase, or both? (lower/upper/both): ").lower()

        return length, special_chars, Options

# Main function using polymorphism
def main():
    # Get inputs from the user
    length, special_chars, Options = Passwor_App.user_input()

    # Polymorphism: Choose generator based on special character option
    if special_chars:
        generator = Complex_Password_Gen(length, Options, special_chars)
    else:
        generator = Simple_Password_Gen(length, Options)

    # Generate and print the password
    password = generator.generate_password()
    print("Generated Password:", password)

# Run the main function
if __name__ == "__main__":
    main()
