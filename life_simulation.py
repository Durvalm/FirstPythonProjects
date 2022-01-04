import random

# Global Variables
age = 0
gross_income = 0
allowance = 0


def personal_info():
    """Ask for user's personal info"""
    global age
    while True:  # Loop Used to ask for name and age again if there's a ValueError
        try:
            name = input("What's your name: ").title().strip()
            age = int(input("What's your age: "))
            break
        except ValueError:
            print("\nTry again, enter an integer for your age.")

    print(f"\nWelcome to the app {name}, we will help you understand your future.")

    return name


def education(name):
    """Ask if user will work or study.
    If studying, for how long user will study before getting a job.
    If working, proceed.
    Upload user's age, and ask if he would like to get a job."""
    global age

    print(f"\nIn our simulation, you are still {age} years old. We want to simulate your next years of life. "
          f"\nThe jobs you will get, money you will keep, and what you will study to get a better job in the future.")

    # Ask if user will study or work
    working_status = input(f"\n{name}, are you gonna keep working in the same kind of job, or take a time "
                           f"to study to get a better one? \nType (W) if working, (S) if studying: ").upper()
    while working_status != "W" and working_status != "S":
        working_status = input(f"\nTry again. (W) for working, (S) For Studying: ").upper()

    #  Increment years of study
    # 0 years of study if user will only work
    if working_status == "W":
        studying_time = 0
        return studying_time
    # Increment prompted amount of years of study if user will take a time to study
    elif working_status == "S":
        while True:
            try:
                studying_time = int(input("For how long will you need to study to get the desired job? (in months): "))
                age += (studying_time / 12)
                break
            except ValueError:
                print("\nError! You need to type an integer.")
        return studying_time


def job(name, studying_time):
    """Ask user what type of job he got, and how much money he will get monthly / Update user's age"""
    global age
    global gross_income

    # If user is already working, pass
    if studying_time == 0:
        pass
    # If user will study for determined amount of time, skip to when he's already working
    else:
        input("\nIf you want to go the future where you already got your desired job, press (Enter): ")
        print(f"{name}, you are currently {age} years old.")

    # Ask user's job and user's gross income
    job_type = input("What's your current profession? ")
    while True:
        try:
            gross_income = int(input("What is your monthly income? "))
            break
        except ValueError:
            print("Try again, enter an integer.")

    return job_type


def mama_help():
    """Ask if user got mama's help, with how much she will help him"""
    global gross_income
    global allowance

    while True:  # While loop to troubleshoot if user doesn't enter an integer
        try:
            allowance = int(input("How much money as a help you get from your parents monthly? (if nothing, type 0): "))
            #  Increment Gross income with allowance, resulting in total income
            gross_income += allowance
            break
        except ValueError:
            print("Error, enter an integer.")


def expenses():
    """prompt and append to expenses' dictionary the main expenses of living alone."""

    print("\nNow it's time to add your expenses.\nAdd the Expenses' Names and Values.")
    # Create dictionary of expenses
    expense = {}
    while True:
        try:
            # Prompt user with expense title and value.  Troubleshoot if ValueError
            expense_title = input("\nEnter Expense's Title: ").title()
            expense_value = int(input("Enter How Much Will You Spend in it Monthly: "))
            expense[expense_title] = expense_value
        except ValueError:
            print("Please, enter an integer where it asks how much you will spend monthly.")

        # Ask if user will add more expenses
        choice = ""
        while choice != "Y" and choice != "N":
            choice = input("Do you want to add more expenses? (Y/N): ").upper()
            # If user will add more expenses, break the inner loop and keep executing outer loop
            if choice == "Y":
                break
            # If user doesn't want to add more expenses, return expenses, this way, breaking both loops
            elif choice == "N":
                return expense
            # If user doesn't type Y or N, keep running inner loop
            else:
                print("Type (Y) for Yes or (N) for No.")


def is_income_enough(name, expense):
    """Check if user can live by his own.  If not possible, ask for more mom's help, or cut expenses.
    If money is enough, proceed.  Display money leftover every month"""
    global age
    global gross_income
    global allowance

    # Get sum of all values in expense dictionary
    expense_total = sum(expense.values())
    # Variable that represents leftover money every month
    net_profit = gross_income - expense_total
    # Print out how much user makes and spends in a month
    print(f"\n{name}, you are currently {age} years old, making {gross_income}$ and spending {expense_total}$ per month.")

    # Give an option to get parent help if net profit is negative
    if net_profit > 1:
        print(f"Congratulations, you save {net_profit}$ every month.")
    else:
        while net_profit < 1:
            print(f"Your balance after each month is negative ({net_profit}$). "
                  f"You should get more help from your parents, or low down some of your expenses."
                  f"\nYou currently get {allowance}$ per month from your parents.")
            # Ask for more help from parents
            while True:
                try:
                    parent_help = int(input(f"How much are your parents gonna add to your allowance? \n(Type 0 if they "
                                            f"can't give more help, "
                                            f"don't worry, you'll have the opportunity to cut off expenses): "))
                    allowance += parent_help
                    net_profit += parent_help
                    gross_income += parent_help
                    break
                except ValueError:
                    print("\nError! Type an integer.")

            # If parents' help is not enough to make a profit, display all expenses
            if net_profit < 1:
                print(f"\nYour net profit is now {net_profit}$, still not enough. Let's cut down some expenses soon.")
                # Display current expenses
                print("\nYour current expenses are:")
                print("--------------------------")
                for key, value in expense.items():
                    print("{0:15} {1}$".format(key, value))

                # Ask if user wants to cut an expense
                while net_profit < 1:
                    print("\nCutting off some expenses...")
                    choice = input("Would you like to cut an expense? (Y/N): ").upper()
                    if choice == "Y":
                        pass
                    elif choice == "N":
                        break
                    else:
                        continue

                    # If user wants to cut an expense, ask which expense to cut
                    while True:
                        expense_cut = input("What expense would you like to cut off: ").title()
                        if expense_cut not in expense.keys():
                            print("\nAdd a listed expense")
                            continue
                        else:
                            break
                    # Ask what value user wants to take off from this expense.
                    while True:
                        try:
                            value_cut = int(input(f"How much would you like to cut off from {expense_cut}: "))
                            expense[expense_cut] -= value_cut
                            net_profit += value_cut
                            break
                        except ValueError:
                            print("\nTry again. Enter an integer!")

                # Print a message if income is enough after expense cutoff
                if net_profit > 1:
                    print(f"Congratulations, you save {net_profit}$ every month.")
                else:
                    print(f"\nYour net profit is {net_profit}$. Not enough for a living!")

            # Break program if parent's help is enough to cover expenses
            else:
                print(f"Congratulations, you save {net_profit}$ every month.")
    return net_profit


def investment(name, job_type, net_profit):
    """Ask how much user wants to invest from what's leftover. If user will invest, give options:
    (mutual funds 10% year),
    (Stock Market, randomly choose % gained from -40% to +40%),
    (Cryptocurrencies, randomly choose % gained from -100% to +100%)"""
    global age

    # Introduce investment options
    print(f"\n{name}, you are working pretty hard as a {job_type}, managing to save {net_profit}$ every month."
          f" It's time to invest. ")
    print("You have 3 types of investment available: Stock Market, Cryptocurrencies, and Mutual Funds.")

    # Ask what type of investment user wants
    investment_choice = input("Which one would you want? (Type 1 for Stock Market, 2 for Crypto, 3 for Mutual Funds,"
                              " and 4 for No investment): ")

    # If user didn't invest, display how much he has saved in 10 years
    if investment_choice == "4":
        non_invested_money = (net_profit * 12) * 10
        print(f"You will have saved {non_invested_money}$ in 10 years.")
        age += 10
        accumulated_income = 0
        return accumulated_income, non_invested_money

    else:
        # Ask how much money user would like to invest
        investment_amount = 9999999999999999
        while investment_amount > net_profit:
            try:
                investment_amount = int(input(f"\nHow much would you like to invest monthly? from 0$ to {net_profit}$: "))
            except ValueError:
                print("Error! Enter an integer.")
        print(f"Great! You will be investing {investment_amount}$ per month.")

        # Ask for how long user will invest
        while True:
            try:
                investment_time = int(input(f"Fow how many years would you like to invest {investment_amount}$? "))
                break
            except ValueError:
                print("\nError! Type an integer.")

        # Get non-invested amount from user
        non_invested_money = ((net_profit - investment_amount) * 12) * investment_time

        # Variables used in next iterations
        year_count = 0
        accumulated_income = investment_amount * 12

        # Display investment result if user invested in Mutual Funds
        if investment_choice == "3":
            while year_count < investment_time:
                # 7% fixed profit rate in Mutual Funds. Update Age and Year Count
                mutual_fund_rate = round(accumulated_income * 0.07, 2)
                year_count += 1
                age += 1
                print(f"\nYear {year_count} of investment in Mutual Funds:"
                      f"\n{name} you are now {age} years old, and finished the year with "
                      f"{round(mutual_fund_rate + accumulated_income, 2)}$")
                print(f"{mutual_fund_rate}$ more than what you would have had if you haven't invested.")

                # Upload interest rate
                accumulated_income += mutual_fund_rate
                if year_count < investment_time - 1:
                    accumulated_income += (investment_amount * 12)

        # Display Investment result if user invested in Crypto
        elif investment_choice == "2":
            while year_count < investment_time:
                # Get a random value for profit in Crypto/ Update Age and Year count
                crypto_rate = round(accumulated_income * (random.randint(-50, 100) / 100), 2)
                year_count += 1
                age += 1
                print(f"\nYear {year_count} of investment in Cryptocurrencies:"
                      f"\n{name} you are now {age} years old, and finished the year with "
                      f"{round(crypto_rate + accumulated_income, 2)}$")

                if crypto_rate > 0:
                    print(f"{crypto_rate}$ more than what you would have had if you haven't invested.")
                else:
                    print(f"You had a {crypto_rate}$ loss.")

                # Upload interest rate
                accumulated_income += crypto_rate
                if year_count < investment_time - 1:
                    accumulated_income += (investment_amount * 12)

        # Display Investment result if user invested in Stocks
        elif investment_choice == "1":
            while year_count < investment_time:
                # Get a random value for profit in Stocks/ Update Age and Year count
                stocks_rate = round(accumulated_income * (random.randint(-20, 40) / 100), 2)
                year_count += 1
                age += 1
                print(f"\nYear {year_count} of investment in the Stock Market:"
                      f"\n{name} you are now {age} years old, and finished the year with "
                      f"{round(stocks_rate + accumulated_income, 2)}$")

                if stocks_rate > 0:
                    print(f"{stocks_rate}$ more than what you would have had if you haven't invested.")
                else:
                    print(f"You had a {stocks_rate}$ loss.")

                # Upload interest rate
                accumulated_income += stocks_rate
                if year_count < investment_time - 1:
                    accumulated_income += (investment_amount * 12)

        return accumulated_income, non_invested_money


def what_to_do_with_money(name, accumulated_income, non_invested_money):
    """Create a dictionary of what user can do with accumulated amount of money, giving ready-made options.
    Only display options that user can afford.
    Prompt user with other things he can do with his money."""
    global age

    input("\nType Anything to Proceed:")
    total_money = round(accumulated_income + non_invested_money, 2)
    print(f"\nHow far you've come {name}, you are {age} years old.")
    print("You have {:,}$ now in your balance, I think it's time for some purchases. ".format(total_money))
    print("Check out some things you can buy.\n------------------------------------------------------------")

    purchases = {
        "1% share in apple": 30000000000,
        "real madrid fc": 1800000000,
        "the mona lisa": 800000000,
        "private island": 14000000,
        "superbowl commercial": 6000000,
        "mansion": 2000000,
        "your kid in harvard": 320000,
        "house": 300000,
        "tesla": 70000,
        "mustang": 30000,
        "3 month vacation": 15000,
        "cheap car": 10000,
        "macbook pro": 3000,
        "pomeranian": 2000,
        "newest iphone": 1000,
    }
    # Display Purchase Options
    for key, value in purchases.items():
        print("{0:25} {1:,}$".format(key, value))

    # Create lists to append Purchases and Prices
    choice = ""
    list_of_purchases = []
    list_of_values = []
    # Ask if user wants to buy something
    while choice != "N":
        choice = input("\nWould you like to buy something? (Y/N): ").upper()
        if choice == "Y":
            purchase = input("What would you like to purchase: ").lower()
            if purchase not in purchases.keys():
                print("Choice is not in the list. Make sure you type it correctly.")
                continue
            # Confirm user's order
            else:
                sure = input(f"Are you sure you want to buy {purchase} for {purchases[purchase]}$? (Y/N): ").upper()
                if sure == "Y" and total_money > purchases[purchase]:
                    list_of_purchases.append(purchase)
                    list_of_values.append(purchases[purchase])
                    total_money -= purchases[purchase]
                    print(f"Your Purchase Was Successful, you have {round(total_money, 2)}$ left.")
                elif total_money < purchases[purchase]:
                    print("You do not have enough money to buy it.")
                else:
                    continue

    # Join both lists together (Purchases and Values)
    print("\nCheck out your purchases below.")
    print("------------------------------------------------")
    zipped_items = zip(list_of_purchases, list_of_values)
    for a, b in zipped_items:
        print("{0:20} {1}$".format(a, b))

    # Give resume
    total_purchasing_cost = sum(list_of_values)
    print(f"\nYou spent {total_purchasing_cost}$ with your purchases")
    print(f"Your Bank Account has {total_money}$ still.")

    if len(list_of_purchases) > 1:
        print(f"{name}, you are {age} years old. I hope you do well with your new stuff, you deserve it.")
    else:
        print(f"{name}, you are {age} years old. I hope you buy something next time.")


def __main__():
    """Call all the functions"""
    user_name = personal_info()
    study_time = education(user_name)
    type_job = job(user_name, study_time)
    mama_help()
    expense_dic = expenses()
    profit = is_income_enough(user_name, expense_dic)
    investment_gains, not_invested_money = investment(user_name, type_job, profit)
    what_to_do_with_money(user_name, investment_gains, not_invested_money)


__main__()
