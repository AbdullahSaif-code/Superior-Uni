# Importing requried modoles
import os # for file opning
import csv # for CSV opreations
from cryptography.fernet import Fernet # for changing or encode password and decode it
from datetime import datetime # for date and time

class FileHandler:
    def __init__(self, csv_file_name="passwords.csv", encryption_key=None):
        self.csv_file_name = csv_file_name

        # Generate or load the encryption key
        if encryption_key:
            self.encryption_key = encryption_key
        else:
            # Save the key for future use
            self.encryption_key = Fernet.generate_key()
            with open("encryption.key", "wb") as key_file:
                key_file.write(self.encryption_key)

        self.cipher = Fernet(self.encryption_key)

        # Ensure the CSV file exists
        if not os.path.exists(self.csv_file_name):
            with open(self.csv_file_name, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["label", "time_of_generation", "password_encrypted"])

    def save_password(self, label, password):
        # Encrypt the password
        encrypted_password = self.cipher.encrypt(password.encode()).decode()
        time_of_generation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(self.csv_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([label, time_of_generation, encrypted_password])
    # Retrived passowrd from CSV
    def retrieve_password(self, label):
        with open(self.csv_file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["label"] == label:
                    original_password = self.cipher.decrypt(row["password_encrypted"].encode()).decode()
                    return {
                        "label": row["label"],
                        "time_of_generation": row["time_of_generation"],
                        "original_password": original_password,
                    }
        return None
    # Delet password from CSV by label / Name
    def delete_password(self, label):
        rows = []
        deleted = False
        with open(self.csv_file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["label"] != label:
                    rows.append(row)
                else:
                    deleted = True

        # If a password was deleted
        if deleted:
            with open(self.csv_file_name, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["label", "time_of_generation", "password_encrypted"])
                writer.writeheader()
                writer.writerows(rows)

        return deleted
    # List all password
    def list_passwords(self):
        saved_passwords = []
        with open(self.csv_file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                saved_passwords.append({
                    "label": row["label"],
                    "time_of_generation": row["time_of_generation"]})
        return saved_passwords
    # Export all passwords to CSV new for back-up
    def export_passwords(self, backup_file_name):
        with open(self.csv_file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            with open(backup_file_name, "w", newline="") as backup_file:
                writer = csv.DictWriter(backup_file, fieldnames=["label", "time_of_generation", "password_encrypted"])
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)