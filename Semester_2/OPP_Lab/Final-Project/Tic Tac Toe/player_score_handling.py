import csv

class PlayerScoreHandling:
    def __init__(self, file_name="player_scores.csv"):
        self.file_name = file_name
        try:
            with open(self.file_name, mode="r") as file:
                pass
        except FileNotFoundError:
            with open(self.file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Player 1", "P1 Score", "Player 2", "P2 Score"])

    def add_player_score(self, player1, p1_score, player2, p2_score):
        with open(self.file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([player1, p1_score, player2, p2_score])

    def display_players(self):
        with open(self.file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  
            print("\n--- Player Scores ---")
            for row in reader:
                print(f"{row[0]}: {row[1]} | {row[2]}: {row[3]}")

    def find_player(self, name):
        found = False
        with open(self.file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader) 
            print(f"\n--- Scores for {name} ---")
            for row in reader:
                if row[0] == name or row[2] == name:
                    print(f"{row[0]}: {row[1]} | {row[2]}: {row[3]}")
                    found = True
        if not found:
            print(f"No scores found for {name}.")

    def delete_player(self, name):
        rows = []
        deleted = False
        with open(self.file_name, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == name or row[2] == name:
                    deleted = True
                else:
                    rows.append(row)
        if deleted:
            with open(self.file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)
            print(f"Player '{name}' and their scores have been deleted.")
        else:
            print(f"Player '{name}' not found.")