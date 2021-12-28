# Encode/Decode Message
print("\n\nType 1 to Encode or 2 to Decode.")
choice = input("Would you like to encode or decode a message: ")

# Dictionary of replaced letters
alphabet = {"a": "яաբ",
            "b": "ч՞՜",
            "c": "ջչշ",
            "d": "شزذجخز",
            "e": "он人",
            "f": "口人",
            "g": "强度",
            "h": "тш",
            "i": "գէթ",
            "j": "ցտս",
            "k": "にな",
            "l": "のは",
            "m": "しご",
            "n": "փք",
            "o": "和约",
            "p": "يو",
            "q": "がき",
            "r": "ヅミ",
            "s": "óöý",
            "t": "ىةٱ",
            "u": "бլխ",
            "v": "شزذ",
            "w": "фрп",
            "x": "йзж",
            "z": "юնյմ",
            " ": "Ղզ",
            ",": "կոգ",
            ".": "っကခ",
            "?": "こဏန",
            "!": "っဘပ",
            ":": "ぬóö",
            "1": "ぢしご",
            "2": "げтш",
            "3": "ッяաբ",
            "4": "ぎон人",
            "5": "なပြအ",
            "6": "ぱ၄၀သ",
            "7": "ぺတပဖ",
            "8": "りヅミ",
            "9": "ゟջչշ",
            "0": "をցփք",
            "'": "ボքսքփ",
            '"': "ロ՝՞՜",
            }
# Encode message
if choice == "1":
    phrase = input("Enter a phrase: ").lower()
    for key, value in alphabet.items():
        phrase = phrase.replace(key, value)
    print(phrase)

elif choice == "2":
    phrase = input("Enter a phrase: ")
    for key, value in alphabet.items():
        phrase = phrase.replace(value, key)
    print(phrase)