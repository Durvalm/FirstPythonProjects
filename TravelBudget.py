# Welcome statement
print("Welcome to the Travel Budget App, pick a city.")

travels = {
   "Kiev": {
       "ticket price": 500,
       "hotel price": 19,
       "food": 9,
       "transportation": 2,
       "language": "Russian"
   },
   "Tallinn": {
       "ticket price": 700,
       "hotel price": 45,
       "food": 28,
       "transportation": 11,
       "language": "Estonian"
   },
   "Sofia": {
       "ticket price": 648,
       "hotel price": 34,
       "food": 15,
       "transportation": 7,
       "language": "Bulgarian"
   },
   "Rome": {
       "ticket price": 605,
       "hotel price": 67,
       "food": 37,
       "transportation": 17,
       "language": "italian"
   },
   "Berlin": {
       "ticket price": 600,
       "hotel price": 57,
       "food": 46,
       "transportation": 16,
       "language": "German"
   },
   "Orlando": {
       "ticket price": 720,
       "hotel price": 112,
       "food": 50,
       "transportation": 48,
       "language": "English"
   },
   "Moscow": {
       "ticket price": 670,
       "hotel price": 39,
       "food": 14,
       "transportation": 6,
       "language": "Russian"
   },
   "Madrid": {
       "ticket price": 478,
       "hotel price": 67,
       "food": 31,
       "transportation": 17,
       "language": "Spanish"
   },
   "London": {
       "ticket price": 579,
       "hotel price": 120,
       "food": 38,
       "transportation": 26,
       "language": "English"
   },
}
# Display prices
print("\nCities    /  Ticket Price  /  Hotel Price  /  Food  /  Transportation  /  language  /")
print("-------------------------------------------------------------------------------------------")
for key, value in travels.items():
    print("{0:10} {1:10}$ {2:13}$ {3:10}$ {4:12}$\t\t\t{5}".format(key, value['ticket price'],
          value['hotel price'], value['food'], value['transportation'], value['language'],))

# Get inputs about trip
running = True
while running:
    days = int(input("\nInput the amount of days you will be traveling: "))
    city = input("Where are you gonna be traveling to: ").title().strip()

    # Calculate/Display Results
    if city in travels.keys():
        cost = travels[city]['ticket price'] + travels[city]['hotel price'] * days + travels[city]['food'] * days + \
               travels[city]['transportation'] * days
        print(f"\n{days} days in {city}. What an awesome choice!\nThe Airplane Ticket will be {travels[city]['ticket price']}$")
        print(f"The Hotel Price will be {travels[city]['hotel price'] * days}$")
        print(f"The Food Cost will be {travels[city]['food'] * days}$")
        print(f"The Transportation Cost will be {travels[city]['transportation'] * days}$")
        print(f"Your Total Cost will be {cost}$")
        print(f"The Language Spoken in {city} is {travels[city]['language']}")
    else:
        continue

    # All travels prices
    print("\nTotal price for all travels: ")
    for k, v in travels.items():
        total_value = travels[k]['ticket price'] + travels[k]['hotel price'] * days + travels[k]['food'] * days + travels[k]['transportation'] * days
        print(f"{k}\t\t   {total_value}$")

    # Change or not destination
    print("\nIf you would like to change your destination, type (yes), otherwise, type (no).")
    choice = input("> ")
    if choice == "yes":
        continue
    elif choice == "no":
        break

    # Add expenses
print(f"\nI love your choice, {city}. Disclaimer:")
print("Every information here is an estimate based on previous travellers' comments. Spending amount varies!")
while True:
    choice = input("\nWould you like to add an expense? (yes/no): ").lower().strip()
    if choice == "no":
        break
    expense = input("Type the expense's title: ").title()
    price = int(input("How much you plan on spending on this expense per day: "))
    travels[city][expense] = price
    new_cost = travels[city][expense]
    cost += new_cost * days
    print(f"Your New Travel Budget is {cost}$")

print("\nHere is Your Updated List of Expenses:")
print("\n" + city + "'s cost: ")

for key, value in travels[city].items():
    total = value * days
    if value == travels[city]["ticket price"]:
        print("{0:15} {1}$".format(key, value))
    if type(value) == int and value != travels[city]["ticket price"]:
        print("{0:15} {1}$".format(key, total))
print("Total{:15}$".format(cost))
print(f"\nThanks For Using The App! I Hope You Enjoy Your Visit To {city}.")