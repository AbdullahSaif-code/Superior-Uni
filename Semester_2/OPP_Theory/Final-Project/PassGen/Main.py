from S_P_G import S_P_G
from C_P_G import C_P_G
from App import Passwor_App
from FileHandler import FileHandler

def main():
    file_handler = FileHandler()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate and Save a Password")
        print("2. Retrieve a Saved Password")
        print("3. Delete a Saved Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":

            length, chars, Options = Passwor_App.user_input()

            # Polymorphism
            if chars:
                generator = C_P_G(length, Options, chars)
            else:
                generator = S_P_G(length, Options)

            password = generator.generate_password()
            print("Generated Password:", password)

            label = input("Enter a label for this password (e.g., 'email', 'bank'): ")
            file_handler.save_password(label, password)
            print(f"Password saved with label: {label}")
            print(f"Password saved as: {password}")

        elif choice == "2":
            label = input("Enter the label of the password to retrieve: ")
            password_data = file_handler.retrieve_password(label)
            if password_data:
                print("Password Details:")
                print(f"Label: {password_data['label']}")
                print(f"Time of Generation: {password_data['time_of_generation']}")
                print(f"Encrypted Password: {password_data['password_encrypted']}")
                print(f"Original Password: {password_data['original_password']}")
            else:
                print("No password found for the given label.")

        elif choice == "3":
            label = input("Enter the label of the password to delete: ")
            deleted = file_handler.delete_password(label)
            if deleted:
                print(f"Password with label '{label}' deleted successfully.")
            else:
                print("No password found for the given label.")

        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()