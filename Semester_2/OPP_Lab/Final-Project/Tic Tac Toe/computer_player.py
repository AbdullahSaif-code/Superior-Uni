from player import Player
import random

class ComputerPlayer(Player):
    def get_move(self, board):
        available_cells = [cell for cell, value in board.cells.items() if value == " "]
        move = random.choice(available_cells)
        print(f"Computer ({self.symbol}) chooses: {move}")
        return move