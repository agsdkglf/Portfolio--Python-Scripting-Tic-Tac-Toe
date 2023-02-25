import random
from art import logo

board = ["#", "#", "#",
            "#", "#", "#",
            "#", "#", "#"]

current_player = "X"
winner = None
is_game_on = True


def numerical_board():
    """Returns the board with the numerical values to inform the player where the numbers are located."""
    print("The board with its numerical values: \n")
    print("\t          ||          ||")
    print("\t     1    ||     2    ||     3")
    print("\t__________||__________||__________")

    print("\t          ||          ||")
    print("\t     4    ||     5    ||     6")
    print("\t__________||__________||__________")

    print("\t          ||          ||")
    print("\t     7    ||     8    ||     9")
    print("\t          ||          ||")
    print("\n")


def board_to_play(board):
    """Returns the playable board."""
    print("The playable board: \n")
    print("\t          ||          ||")
    print("\t     {}    ||     {}    ||     {}"f"(board[0], board[1], board[2])")
    print("\t__________||__________||__________")

    print("\t          ||          ||")
    print("\t     {}    ||     {}    ||     {}"f"(board[0], board[1], board[2])")
    print("\t__________||__________||__________")

    print("\t          ||          ||")
    print("\t     {}    ||     {}    ||     {}"f"(board[0], board[1], board[2])")
    print("\t          ||          ||")
    print("\n")


def player_move(board):
    """Allows the player to make the move."""
    player_choice = int(input(f"Player {current_player} select a value from one to nine: "))
    if board[player_choice - 1] == "#":
        board[player_choice - 1] = current_player
    else:
        print("The place you selected is already taken.")


def winner_vertically(board):
    """Checks whether the player wins vertically."""
    global winner
    if board[0] == board[3] == board[6] and board[3] != "#":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "#":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "#":
        winner = board[5]
        return True


def winner_horizontally(board):
    """Checks whether the player wins horizontally."""
    global winner
    if board[0] == board[1] == board[2] and board[2] != "#":
        winner = board[2]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "#":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "#":
        winner = board[7]
        return True


def winner_diagonally(board):
    """Checks whether the player wins diagonally."""
    global winner
    if board[0] == board[4] == board[8] and board[4] != "#":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "#":
        winner = board[4]
        return True


def check_winner(board):
    """Checks whether there's a draw or who's the winner of the game."""
    global is_game_on

    for _ in range(9):

        if winner_vertically(board):
            print(f"\nThe winner is: {winner}! Congratulations 👏")
            is_game_on = False
            break

        elif winner_horizontally(board):
            print(f"\nThe winner is: {winner}! Congratulations 👏")
            is_game_on = False
            break

        elif winner_diagonally(board):
            print(f"\nThe winner is: {winner}! Congratulations 👏")
            is_game_on = False
            break

        elif "#" not in board:
            print("\nIt's a draw!")
            is_game_on = False
            break


def player():
    """Allows to switch the players."""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer_player(board):
    """Allows a computer as a player we play with."""
    while current_player == "O":
        computer_position = random.randint(0, 8)
        if board[computer_position] == "#":
            board[computer_position] = "O"
            player()


while is_game_on:
    print(logo)
    numerical_board()
    board_to_play(board)
    player_move(board)
    check_winner(board)
    player()
    computer_player(board)
    board_to_play(board)
    check_winner(board)
