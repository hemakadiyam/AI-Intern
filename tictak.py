import math

def print_board(board):
    print("\n")
    print(" | ".join(board[0:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]))
    print("\n")

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all([spot == "X" or spot == "O" for spot in board])

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [" " for _ in range(9)]
    human_player = "X"
    ai_player = "O"
    current_player = "X"

    while True:
        print_board(board)
        if current_player == human_player:
            move = input(f"Player {current_player}, choose a position (1-9): ")
            if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] != " ":
                print("Invalid move. Try again.")
                continue
            board[int(move) - 1] = current_player
        else:
            print("AI is making a move...")
            move = best_move(board)
            board[move] = ai_player

        if check_win(board, current_player):
            print_board(board)
            if current_player == human_player:
                print(f"Congratulations! Player {current_player} wins!")
            else:
                print("AI wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
