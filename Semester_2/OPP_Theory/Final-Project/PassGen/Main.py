#  Data Abstraction for code handling and simplecity
import os
from S_P_G import S_P_G
from C_P_G import C_P_G
from App import Passwor_App
from FileHandler import FileHandler

#  Main Menu Code
def main():
    file_handler = FileHandler()
    while True:
        print("\nMain menu:")
        print("1. Generate Password")
        print("2. Retrieve Password")
        print("3. Delete Password")
        print("4. List Passwords")
        print("5. Open CSV")
        print("6. Export Passwords")
        print("7. Exit")
        choice = input("Enter your choice: ")

        #  Genrate Password
        if choice == "1":
            length, chars, Options = Passwor_App.user_input()
            if chars:
                generator = C_P_G(length, Options, chars)
            else:
                generator = S_P_G(length, Options)
            password = generator.generate_password()
            print("Generated Password:", password)

            #  Label / Name Password
            label = input("Enter a label for this password: ")
            file_handler.save_password(label, password)
            print(f"Password saved successfully with label: {label}")

        #  Retrive saved Password
        elif choice == "2":
            label = input("Enter the label of the password to retrieve: ")
            password_data = file_handler.retrieve_password(label)
            if password_data:
                print("Password Details:")
                print(f"Label: {password_data['label']}")
                print(f"Time of Generation: {password_data['time_of_generation']}")
                print(f"Original Password: {password_data['original_password']}")
            else:
                print("No password found.")

        # Delete saved password
        elif choice == "3":
            label = input("Enter the label to delete: ")
            deleted = file_handler.delete_password(label)
            if deleted:
                print(f"Password '{label}' deleted successfully.")
            else:
                print("No password found.")

        # List all saved password
        elif choice == "4":
            saved_passwords = file_handler.list_passwords()
            if saved_passwords:
                print("\nSaved Passwords:")
                for index, password_data in enumerate(saved_passwords, start=1):
                    print(f"{index}. Label: {password_data['label']} | Time: {password_data['time_of_generation']}")
            else:
                print("No passwords found.")

        # Open CSV
        elif choice == "5":
            csv_file_name = "passwords.csv"
            if os.path.exists(csv_file_name):
                print(f"Opening {csv_file_name}")
                os.startfile(csv_file_name)
            else:
                print("No CSV file found.")


        # Make backup copy of password
        elif choice == "6":
            export_file_name = input("Enter the name of the backup file:")
            file_handler.export_passwords(export_file_name)
            print(f"Passwords have been exported to {export_file_name}.")

        # Exit
        elif choice == "7":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice.")
#  To run Main function
if __name__ == "__main__":
    main()