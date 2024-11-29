from board import Board

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],[3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.scores = {self.player1.name: 0, self.player2.name: 0}

    def check_winner(self):
        for combo in self.win_combos:
            if all(self.board.cells[cell] == self.current_player.symbol for cell in combo):
                return True
        return False

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play_game(self):
        self.board.reset()
        while True:
            self.board.display()
            move = self.current_player.get_move(self.board)
            self.board.update(move, self.current_player.symbol)
            if self.check_winner():
                self.board.display()
                print(f"Congratulations {self.current_player.name}! You have won the game.")
                self.scores[self.current_player.name] += 1
                break
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            self.switch_player()

    def display_scores(self):
        print("\nSCOREBOARD:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")
        print()