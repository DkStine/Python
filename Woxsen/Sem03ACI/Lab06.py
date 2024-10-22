import numpy as np
import math

# Define constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6]   
    ]
    indices = [i for i in range(9) if board[i] == player]
    for condition in win_conditions:
        if all(i in indices for i in condition):
            return True
    return False

# Evaluate the board for terminal states
def evaluate(board):
    if is_winner(board, PLAYER_X):
        return 1
    if is_winner(board, PLAYER_O):
        return -1
    return 0

# Check if the board is full
def is_full(board):
    return all(cell != EMPTY for cell in board)

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    if score == 1:
        return score
    if score == -1:
        return score
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Find the best move for the current player
def find_best_move(board):
    best_move = -1
    best_value = -math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            move_value = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if move_value > best_value:
                best_move = i
                best_value = move_value
    return best_move

# Print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Main function to play the game
def play_game():
    board = [EMPTY] * 9
    current_player = PLAYER_X

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            move = find_best_move(board)
            if move == -1:
                print("It's a draw!")
                break
        else:
            move = int(input(f"Player {PLAYER_O}'s turn (0-8): "))
            if board[move] != EMPTY:
                print("Invalid move, try again.")
                continue

        board[move] = current_player
        if evaluate(board) != 0:
            print_board(board)
            if current_player == PLAYER_X:
                print("Player X wins!")
            else:
                print("Player O wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Run the game
if __name__ == "__main__":
    play_game()