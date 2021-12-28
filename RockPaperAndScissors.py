import random
print("Welcome to the game of Rock, Paper, Scissors")

# Define Variables: Rounds played and List of options
rounds = int(input("\nHow many rounds would you like to play: "))
lst_game = ["rock", "paper", "scissors"]

# Define Variables: Player Points, PC Points, Tie
point_player = 0
point_pc = 0
tie = 0

# Loop through total number of rounds
for number in range(rounds):
    print(f"\nRound {number + 1}")
    print(f"Player: {point_player}\t\tComputer: {point_pc}")

# Get input (player choice), define computer choice (random).
    player_choice = input("Time to pick...rock, paper, scissors: ").lower().strip()
    computer_choice = random.choice(lst_game)

# Simulate Game
    # Player wins
    if player_choice in lst_game:
        if player_choice == "rock" and computer_choice == "scissors":
            point_player += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{player_choice} breaks {computer_choice}\n\tYou win round {number + 1}.")
        elif player_choice == "scissors" and computer_choice == "paper":
            point_player += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{player_choice} cuts {computer_choice}\n\tYou win round {number + 1}.")
        elif player_choice == "paper" and computer_choice == "rock":
            point_player += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{player_choice} rolls {computer_choice}\n\tYou win round {number + 1}.")
        # Tie
        elif player_choice == computer_choice:
            tie += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\tIt's a tie, how boring!\n\tThis round was a tie")
        # Computer Wins
        elif player_choice == "rock" and computer_choice == "paper":
            point_pc += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{computer_choice} rolls {player_choice}\n\tComputer gets the point.")
        elif player_choice == "scissors" and computer_choice == "rock":
            point_pc += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{computer_choice} destroys {player_choice}\n\tComputer gets the point.")
        elif player_choice == "paper" and computer_choice == "scissors":
            point_pc += 1
            print(f"\tPlayer: {player_choice}\n\tComputer: {computer_choice}"
                  f"\n\t{computer_choice} cuts {player_choice}\n\tComputer gets the point.")
    else:
        point_pc += 1
        print("\tThat is not a valid game option!")

# Print game results
print("\n\nFinal Game Results:")
print(f"\tRounds Played: {number + 1}")
print(f"\tPlayer Score: {point_player}")
print(f"\tComputer Score: {point_pc}")
print(f"\tTies: {tie}")

if point_pc > point_player:
    print(f"\tWinner: Computer")
elif point_pc < point_player:
    print(f"\tWinner: Player")
elif point_pc == point_player:
    print(f"\tIt's a tie")

# Print percentage
print("\nPercentage of Victory:")
percentage_player = (point_player / (number + 1)) * 100
percentage_computer = (point_pc / (number + 1)) * 100
percentage_tie = (tie / (number + 1)) * 100
print(f"\nPercentage of Player Wins: \t{round(percentage_player, 2)}%")
print(f"Percentage of Computer Wins: \t{round(percentage_computer, 2)}%")
print(f"Percentage of Ties: \t{round(percentage_tie, 2)}%")