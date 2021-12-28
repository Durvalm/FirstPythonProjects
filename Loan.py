from matplotlib import pyplot


def get_loan_info():
    """Get the basic information of a loan and store it in a dictionary"""
    # Create a blank dictionary to put loan info
    loan = {}

    # Get user input for categories of the loan
    loan["principal"] = float(input("\nEnter the loan amount: "))
    loan["rate"] = float(input("Enter the interest rate: "))
    loan['down payment'] = float(input("What would you like to put as a down payment: "))
    loan["monthly payment"] = float(input("Enter the monthly payment amount: "))
    loan["money paid"] = loan['down payment']
    loan["hoa"] = float(input("How much will you pay on HOA per month: "))
    loan["insurance"] = loan["principal"] * 0.0035 / 12
    loan["property tax"] = loan["principal"] * 0.0098 / 12
    loan["principal"] -= loan['down payment']

    return loan


def make_payment(loan, initial_principle, initial_insurance, initial_tax, initial_hoa):
    """Determine Loan Information as payments Happen"""

    # Add value to variables every month
    loan["insurance"] += initial_insurance
    loan["property tax"] += initial_tax
    loan["hoa"] += initial_hoa

    # Determine factor paid every month
    monthly_factor = ((loan["rate"] / 100) / 12) * loan["principal"]
    other_costs = initial_insurance + initial_tax + initial_tax

    # Update Principal Paid value for every Payment
    loan["principal"] = loan["principal"] + monthly_factor + other_costs - loan["monthly payment"]

    # Update money paid value for every Payment
    if loan["principal"] > 0:
        loan["money paid"] += (loan["monthly payment"] + other_costs)
    # If principle goes negative, update principle's and money paid's values
    else:
        loan["money paid"] += loan['monthly payment'] + loan["principal"]
        loan["principal"] = 0


def display_info(loan, month_count):
    """Display the current loan status"""
    print(f"\n----Loan information after {month_count} months----")
    for key, value in loan.items():
        print(f"{key.title()}: {round(value,2)}")


def summarize_loan(loan, month_count, initial_principal):
    """Display the results of paying off the loan"""
    print("\n\n--------------------------------------------------------------------------------------")
    print(f"Congratulations, you paid off your loan in {month_count} months ({round(month_count / 12, 1)} years)!")
    print(f"Your initial loan was ${initial_principal + loan['down payment']}, at a rate of {loan['rate']}%.")
    print(f"Your monthly payment was ${loan['monthly payment']}.")
    print(f"You spent ${round(loan['money paid'], 2)} in total.")

    # Calculate value paid on interest+taxes
    cost = round(loan['money paid'] - initial_principal - loan['down payment'], 2)
    print(f"You spent ${cost} on interest, Taxes, HOA and Insurance.")


def create_graph(data, loan):
    """Create a graph to show the relationship between Principal and Time"""
    x_values = []   # These represent month numbers
    y_values = []   # These represent corresponding principal values

    # Loop through data set
    # Point[0] represents a month number, point[1] represents the principal value
    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])

    # Create a plot for x_values and y_values (month number and principle)
    pyplot.plot(x_values, y_values)
    pyplot.title(str(loan['rate']) + "% Interest With $" + str(loan['monthly payment']) + " Monthly Payment.")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")

    # Display created graph
    pyplot.show()


# The main code
print("Welcome to the Loan Calculator App")
# Initialize variables
my_loan = get_loan_info()
month = 1

starting_principal = my_loan['principal']
starting_insurance = my_loan['insurance']
starting_tax = my_loan["property tax"]
starting_hoa = my_loan["hoa"]


data_to_plot = []

display_info(my_loan, month)
input("Press Enter to start paying off the loan!")
# Loop through every payday
while my_loan['principal'] != 0:
    # Increment month number, make payments, display info, append (month and principal) to plot
    month += 1
    make_payment(my_loan, starting_principal, starting_insurance, starting_tax, starting_hoa)
    display_info(my_loan, month)
    data_to_plot.append((month, my_loan['principal']))

    # Stop running if monthly payment is not enough to cover the interest rate
    if my_loan['principal'] > starting_principal:
        print("\nMonthly payment is not enough to cover the interest rate.")
        break

# if loan is paid off, summarize loan.
# Month > 1, because if it's not possible to pay off the loan, it's gonna loop only 1 time, if it loops more than 1 time
# it means that the loan can be paid off
if month > 1:
    summarize_loan(my_loan, month, starting_principal)
    # Call function to display graph
    create_graph(data_to_plot, my_loan)
