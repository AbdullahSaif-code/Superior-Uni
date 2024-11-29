from human_player import HumanPlayer
from computer_player import ComputerPlayer
from tic_tac_toe import TicTacToeGame
from player_score_handling import PlayerScoreHandling

def menu():
    scores = PlayerScoreHandling()
    while True:
        print("\n---: Welcome to Tic Tac Toe :---")
        print("1. Play with a friend")
        print("2. Play against the computer")
        print("3. Display player scores")
        print("4. Find Player")
        print("5. Delete player score")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice in [1, 2]:
                player1_name = input("Enter Player 1's name: ").strip()
                player2_name = input("Enter Player 2's name: ").strip() if choice == 1 else "Computer"
                player1 = HumanPlayer(player1_name, 'X')
                player2 = HumanPlayer(player2_name, 'O') if choice == 1 else ComputerPlayer(player2_name, 'O')
                game = TicTacToeGame(player1, player2)
                playing = True  

                while playing:  
                    game.play_game()
                    game.display_scores()  
                    game.switch_player() 
                
                    while True: 
                        again = input("Do you want to play again? (y/n): ").strip().lower()
                        if again == "y":
                            break
                        elif again == "n":
                            
                            scores.add_player_score(
                                game.player1.name, game.scores[game.player1.name],
                                game.player2.name, game.scores[game.player2.name]
                            )
                            playing = False 
                            break 
                        else:
                            print("Invalid input. Please enter 'y' to play again or 'n' to exit.")
                            
            elif choice == 3:
                scores.display_players()
                
            elif choice == 4:
                name = input("Enter the player's name to find: ").strip().title()
                scores.find_player(name)
                
            elif choice == 5:
                name = input("Enter the player's name to delete: ").strip().title()
                scores.delete_player(name)
                
            elif choice == 6:
                print("    Thanks for playing!")
                break
                
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    menu()
