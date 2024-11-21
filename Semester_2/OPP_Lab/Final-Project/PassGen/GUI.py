import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
from FileHandler import FileHandler
from S_P_G import S_P_G
from C_P_G import C_P_G

# Initialize FileHandler
file_handler = FileHandler()

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        # Main Menu Buttons
        tk.Label(root, text="Password Manager", font=("Arial", 16)).pack(pady=10)
        tk.Button(root, text="Generate Password", command=self.generate_password_gui).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Retrieve Password", command=self.retrieve_password_gui).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Delete Password", command=self.delete_password_gui).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="List Passwords", command=self.list_passwords_gui).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Open CSV", command=self.open_csv).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Export Passwords", command=self.export_passwords_gui).pack(fill="x", padx=20, pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(fill="x", padx=20, pady=5)

    def generate_password_gui(self):
        generate_window = tk.Toplevel(self.root)
        generate_window.title("Generate Password")

        # Inputs for password generation
        tk.Label(generate_window, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
        length_entry = tk.Entry(generate_window)
        length_entry.grid(row=0, column=1, padx=5, pady=5)

        options = {"Uppercase": tk.BooleanVar(),
                   "Lowercase": tk.BooleanVar(),
                   "Digits": tk.BooleanVar(),
                   "Special Characters": tk.BooleanVar()}
        
        row = 1
        for option, var in options.items():
            tk.Checkbutton(generate_window, text=option, variable=var).grid(row=row, column=0, columnspan=2, sticky="w", padx=5)
            row += 1

        tk.Label(generate_window, text="Custom Characters (Optional):").grid(row=row, column=0, padx=5, pady=5)
        chars_entry = tk.Entry(generate_window)
        chars_entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        tk.Label(generate_window, text="Label for Password:").grid(row=row, column=0, padx=5, pady=5)
        label_entry = tk.Entry(generate_window)
        label_entry.grid(row=row, column=1, padx=5, pady=5)

        def generate_and_save():
            length = int(length_entry.get()) if length_entry.get().isdigit() else 8
            chars = chars_entry.get()
            label = label_entry.get()

            selected_options = {key: var.get() for key, var in options.items()}
            if chars:
                generator = C_P_G(length, selected_options, chars)
            else:
                generator = S_P_G(length, selected_options)
            
            password = generator.generate_password()
            file_handler.save_password(label, password)
            messagebox.showinfo("Success", f"Generated Password: {password}")

        tk.Button(generate_window, text="Generate and Save", command=generate_and_save).grid(row=row+1, column=0, columnspan=2, pady=10)

    def retrieve_password_gui(self):
        retrieve_window = tk.Toplevel(self.root)
        retrieve_window.title("Retrieve Password")

        tk.Label(retrieve_window, text="Enter Label:").pack(pady=5)
        label_entry = tk.Entry(retrieve_window)
        label_entry.pack(pady=5)

        def retrieve():
            label = label_entry.get()
            data = file_handler.retrieve_password(label)
            if data:
                messagebox.showinfo("Password Retrieved",
                                    f"Label: {data['label']}"
                                    f"Time: {data['time_of_generation']}"
                                    f"Password: {data['original_password']}")
            else:
                messagebox.showerror("Error", "No password found for the given label.")

        tk.Button(retrieve_window, text="Retrieve", command=retrieve).pack(pady=10)

    def delete_password_gui(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Password")

        tk.Label(delete_window, text="Enter Label:").pack(pady=5)
        label_entry = tk.Entry(delete_window)
        label_entry.pack(pady=5)

        def delete():
            label = label_entry.get()
            if file_handler.delete_password(label):
                messagebox.showinfo("Success", f"Password with label '{label}' deleted.")
            else:
                messagebox.showerror("Error", "No password found for the given label.")

        tk.Button(delete_window, text="Delete", command=delete).pack(pady=10)

    def list_passwords_gui(self):
        list_window = tk.Toplevel(self.root)
        list_window.title("List Passwords")

        passwords = file_handler.list_passwords()
        if passwords:
            for password_data in passwords:
                tk.Label(list_window, text=f"Label: {password_data['label']}, Time: {password_data['time_of_generation']}").pack(anchor="w")
        else:
            tk.Label(list_window, text="No passwords found.").pack(pady=10)

    def open_csv(self):
        csv_file_name = file_handler.csv_file_name
        if os.path.exists(csv_file_name):
            os.startfile(csv_file_name)
        else:
            messagebox.showerror("Error", "CSV file does not exist.")


    def export_passwords_gui(self):
        export_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if export_file:
            file_handler.export_passwords(export_file)
            messagebox.showinfo("Success", f"Passwords exported to {export_file}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
