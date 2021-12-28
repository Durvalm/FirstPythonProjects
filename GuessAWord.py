import random
print("Welcome to the Guess My Word App")

# Categories
categories = {
   "Sports": ["football", "basketball", "tennis", "golf", "cricket", "hockey", "table tennis", "volleyball", "rugby",
              "badminton", "wrestling", "skateboarding", "boxing", "bowling"],
   "Fruits": ["strawberry", "banana", "apple", "mango", "orange", "watermelon", "tomato", "pear", "avocado",
              "pineapple", "melon", "papaya"],
   "Famous Players": ["ronaldo", "beckham", "messi", "zidane", "michael jordan", "kobe", "shevchenko", "ronaldinho", "neymar",
                      "ibrahimovic", "lebron james", "maradona", "pele", "kaka", "thierry henry", "pirlo", "pogba"],
   "Cities": ["vienna", "orlando", "warsaw", "moscow", "miami", "san diego", "paris", "rome", "london", "berlin",
              "sofia", "brussels", "lisbon", "madrid", "amsterdam", "prague", "minsk", "bratislava", "budapest",
              "sarajevo", "athens", "belgrade", "dublin", "oslo", "kiev", "bucharest", "tallinn"]
   }

# Create a list of keys
category_keys = []
for key in categories.keys():
    category_keys.append(key)

# Main game loop
running = True
while running:
    key_random = random.choice(category_keys)
    if key_random in categories:
        value_random = random.choice(categories[key_random])
    print(f"\nGuess a {len(value_random)} word from the following category: {key_random}")

    # Hidden word
    hidden_word = []
    for i in value_random:
        hidden_word.append("-")

    # Guess
    guess = ""
    guess_count = 0

    # A single round loop
    while guess != value_random:
        print("".join(hidden_word))
        guess = input("\nEnter your guess: ").lower().strip()
        guess_count += 1

        if guess_count == len(value_random):
            print(f"You couldn't solve the problem. the right word was {value_random}")
            break

        if guess == value_random:
            print(f"\nCorrect! You guessed the word in {guess_count} guesses.")
            break
        else:
            print("That is not correct, let us review a letter to help you!")
            # Loop to replace dash in hidden_string
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(value_random)-1)
                if hidden_word[letter_index] == "-":
                    hidden_word[letter_index] = value_random[letter_index]
                    swapping = False

    choice = input("\nWould you like to play again (y/n): ").lower()
    if choice == "n":
        break