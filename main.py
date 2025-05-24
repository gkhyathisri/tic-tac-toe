import math
import random

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check for a win
def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row, col in get_available_moves(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row, col in get_available_moves(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
        return best_score

# AI move
def best_move(board):
    best_score = -math.inf
    move = None
    for row, col in get_available_moves(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            move = (row, col)
    return move

# Game Loop
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player Move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"
        print_board(board)

        if is_winner(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI Move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print("Computer played:")
        print_board(board)

        if is_winner(board, "O"):
            print("Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play()
