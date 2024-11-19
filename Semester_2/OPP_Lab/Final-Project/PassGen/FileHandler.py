import os
import csv
from cryptography.fernet import Fernet
from datetime import datetime

class FileHandler:
    def __init__(self, csv_file_name="passwords.csv", encryption_key=None):
        self.csv_file_name = csv_file_name

        if encryption_key:
            self.encryption_key = encryption_key
        else:
            self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

        if not os.path.exists(self.csv_file_name):
            with open(self.csv_file_name, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["label", "time_of_generation", "password_encrypted", "original_password"])

    def save_password(self, label, password):

        time_of_generation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        encrypted_password = self.cipher.encrypt(password.encode()).decode()

        with open(self.csv_file_name, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([label, time_of_generation, encrypted_password, password])

    def retrieve_password(self, label):

        with open(self.csv_file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["label"] == label:

                    decrypted_password = self.cipher.decrypt(row["password_encrypted"].encode()).decode()
                    return {
                        "label": row["label"],
                        "time_of_generation": row["time_of_generation"],
                        "password_encrypted": row["password_encrypted"],
                        "original_password": decrypted_password,
                    }
        return None

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


        with open(self.csv_file_name, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["label", "time_of_generation", "password_encrypted", "original_password"])
            writer.writeheader()
            writer.writerows(rows)

        return deleted
