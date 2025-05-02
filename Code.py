# Tic-Tac-Toe Game in Python

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-" * 5)

# Function to check if a player has won
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"
    
    while True:
        print_board()
        
        # Get player input
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        
        if board[move] != " ":
            print("That spot is already taken, try again.")
            continue
        
        board[move] = current_player
        
        # Check for winner
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (draw)
        if is_board_full():
            print_board()
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
