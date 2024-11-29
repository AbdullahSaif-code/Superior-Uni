from player import Player

class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid move. Choose a number between 1 and 9.")
                elif board.cells[move] != " ":
                    print("This cell is already occupied. Try again.")
                else:
                    return move
            except ValueError:
                print("Invalid input. Please enter a number.")