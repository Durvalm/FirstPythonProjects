import random
print("------------------------Power-Ball Simulator--------------------------")

# Variables
interval = []
winning_numbers = []

# Getting user input
running = True
while running:
    drawing_white = int(input("\nHow many white-balls to draw from for the 5 winning numbers (normally 69): "))
    drawing_red = int(input("How many red-balls to draw from for the Power-Ball (normally 26): "))
    if drawing_white not in range(1, 70) or drawing_red not in range(1, 27):
        print("Values need to be below (69) and (26).")
    else:
        running = False

# Determining winning White-Balls
while len(winning_numbers) < 5:
    winning_white = random.randint(1, drawing_white)
    if winning_white not in winning_numbers:
        winning_numbers.append(winning_white)
winning_numbers.sort()

# Determining Winning Red-Balls
winning_red = random.randint(1, drawing_red)
winning_numbers.append(winning_red)

# calculate odds of winning/Formatting it
odds = 1
for i in range(5):
    odds *= drawing_white - i
odds *= drawing_red/120
odds_formatted = "{:,}".format(odds)

# Determining the Jackpot/ formatting values
jackpot = round(odds * 1.2, 2)
jackpot_formatted = "{:,}".format(jackpot)
print(f"The Current Jackpot is {jackpot_formatted}$")
print(f"\nYou have a 1 in {odds_formatted} chance of winning this lottery.")

# input amount of tickets user will buy
print("Each ticket costs 2$, how many tickets do you want to buy?")
ticket = int(input("Enter the amount of tickets you will purchase: "))
interval.append(ticket)

# Display Powerball game
print("\n------------  Welcome to the Power-Ball  ------------")
print(f"\nTonight's winning numbers are: {winning_numbers}")
input("Press 'Enter' to begin purchasing tickets!!!")

# Count Amount of tickets sold, and determine list to append all bets
tickets_sold = 0
bets = []

# Main Powerball Game
while tickets_sold < sum(interval):
    my_bet = []

    # Get Random Values for each white ball list
    while len(my_bet) < 5:
        bet_white = random.randint(1, drawing_white)
        if bet_white not in my_bet:
            my_bet.append(bet_white)
    my_bet.sort()

    # Get Random Values for each Powerball number
    bet_red = random.randint(1, drawing_red)
    my_bet.append(bet_red)

    # If Bet was already used before, disregard it.
    if my_bet not in bets:
        tickets_sold += 1
        bets.append(my_bet)
        print(my_bet)
        # Determine price of tickets
        price = tickets_sold * 2
        price_formatted = "{:,}".format(price)

    # Break loop if user win the lottery
    if my_bet == winning_numbers:
        print(f"You won the lottery with {tickets_sold} tries, costing you {price_formatted}$. Congratulations! ")
        print(f"You won the prize of {jackpot_formatted}$")
        break

    # Show amount of tickets purchased
    if tickets_sold == sum(interval):
        print(f"{sum(interval)} tickets purchased so far with no winners, you have spent {price_formatted}$.")
        # Ask user if he would like to play again
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice == "y":
            interval.append(ticket)
            continue

        elif choice == "n":
            print(f"Thanks for playing!, you have spent {price_formatted}$.")
            break
