def draw_board(char_list):
    """Print a game board; either a number board or a tic tac toe board."""
    print("\n\t\tTic-Tac-Toe")
    print("\t-------------------")
    print(f"\t|  {char_list[0]}  |  {char_list[1]}  |  {char_list[2]}  |")
    print("\t-------------------")
    print(f"\t|  {char_list[3]}  |  {char_list[4]}  |  {char_list[5]}  |")
    print("\t-------------------")
    print(f"\t|  {char_list[6]}  |  {char_list[7]}  |  {char_list[8]}  |")
    print("\t-------------------")


def get_player_input(player_char, char_list):
    """Get players move until it is a valid move on the board with no piece currently there."""
    # Get user input
    while True:
        player_move = int(input(f"{player_char}: Where would you like to place your piece (1-9): "))
        # Move is on board
        if 0 < player_move < 10:
            # Move is an empty spot
            if char_list[player_move - 1] == "_":
                return player_move
            else:
                print("That spot has already been chosen.  Try again.")
        else:
            print("That is not a spot on the board.  Try again.")


def place_char_on_board(player_char, player_move, char_list):
    """Put a players character at the correct spot on the board."""
    char_list[player_move - 1] = player_char


def is_winner(player_char, char_list):
    """Return a Bool if the given player is a winner."""
    return((char_list[0] == player_char and char_list[1] == player_char and char_list[2] == player_char) or # FIRST ROW
           (char_list[3] == player_char and char_list[4] == player_char and char_list[5] == player_char) or # SECOND ROW
           (char_list[6] == player_char and char_list[7] == player_char and char_list[8] == player_char) or # LAST ROW
           (char_list[0] == player_char and char_list[3] == player_char and char_list[6] == player_char) or # FIRST COLUMN
           (char_list[1] == player_char and char_list[4] == player_char and char_list[7] == player_char) or # SECOND COLUMN
           (char_list[2] == player_char and char_list[5] == player_char and char_list[8] == player_char) or # LAST COLUMN
           (char_list[0] == player_char and char_list[4] == player_char and char_list[8] == player_char) or # FIRST DIAGONAL
           (char_list[2] == player_char and char_list[4] == player_char and char_list[6] == player_char)) # SECOND DIAGONAL


# The Main Code
# Define Variables
player1 = 'X'
player2 = 'O'
n_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
c_list = ["_"] * 9

# Draw the initial state of the game
draw_board(n_list)
draw_board(c_list)

while True:
    # Player1 turn
    # Get the players move
    move = get_player_input(player1, c_list)
    # Move on board
    place_char_on_board(player1, move, c_list)
    # Re-draw the board
    draw_board(n_list)
    draw_board(c_list)
    # Check to see if player 1 won ot it is a tie
    if is_winner(player1, c_list):
        print("Player 1 wins")
        break
    # Check if there is a tie
    elif "_" not in c_list:
        print("The game was a tie!")
        break

    # Player 2 turn
    # Get the players move
    move = get_player_input(player2, c_list)
    # Move on board
    place_char_on_board(player2, move, c_list)
    # Re-draw the board
    draw_board(n_list)
    draw_board(c_list)
    # Check if player 2 won
    if is_winner(player2, c_list):
        print("Player 2 wins!")
        break
