# N-Queen Problem Solution
def print_board(board):
    for row in board:
        print(' '.join('Q' if col else '.' for col in row))
    print()

def is_safe(board, row, col):
    n = len(board)
    # Check this column on upper side
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_util(board, row, solutions):
    n = len(board)
    if row == n:
        # Found a solution
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens_util(board, row+1, solutions)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions

def main():
    n = int(input("Enter the value of N for N-Queen problem: "))
    solutions = solve_n_queens(n)
    print(f"Total solutions for N={n}: {len(solutions)}")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_board(sol)

if __name__ == "__main__":
    main()
choice = int(input("Enter number to creat matrix: "))



def print_solution(choice):
    for i in range(choice):
        for j in range(choice):
            print("   ",end="")
            if j < choice-1:
                print("|",end="")
        print()
        if i <choice-1:
            for j in range(choice):
                print("- -",end="")
                if j < choice-1:
                    print(" ", end="")
            print()

def solve(choice):
    print_solution(choice)
    print(f"Matrix of size {choice}x{choice} created.")


def is_safe():
    choice = int(input("Enter the value of N for N-Queen problem: "))
    solutions = solve_n_queens(choice)
    print(f"Total solutions for N={choice}: {len(solutions)}")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_board(sol)


def main():
    while True:
        print (f"Dyanamic N-Queens Problem")
        print(f"1. For run.")
        print(f"2. Exit.")
        user_input = int(input("Enter option: "))
        if user_input == 1:
            is_safe()
        elif user_input == 2:
            break
        else:
            print("Enter Corect Option.")

main()