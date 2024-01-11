"""
engeto_projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jana Fleišerová
email: fleiserova.jana@gmail.com
discord: Jana F.
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

'''
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
'''

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
separator = "-------------------------------------------------"

name = input("Enter user name: ")

if name in users.keys():
    password = input("Enter your password: ")

    if password == users[name]:
        print(separator, f"Welcome to the app, {name}", "We have 3 texts to be analyzed.", separator, sep="\n")
        input_number = input("Enter a number btw. 1 and 3 to select: ")
        print(separator)

        if (input_number).isdigit():
            number = int(input_number)

            if number <= 3:
                words = []

                for word in TEXTS[number - 1].split():
                    words.append(word.strip(",."))
                count = len(words)
                print(f"There are {count} words in the selected text.")

                title_words = []
                for word in words:
                    if word.istitle():
                        title_words.append(word)
                title_count = len(title_words)
                print(f"There are {title_count} titlecase words.")

                upper_words = []
                for word in words:
                    if word.isupper() and word.isalpha():
                        upper_words.append(word)
                upper_count = len(upper_words)
                print(f"There are {upper_count} uppercase words.")

                lower_words = []
                for word in words:
                    if word.islower() and word.isalpha():
                        lower_words.append(word)
                lower_count = len(lower_words)
                print(f"There are {lower_count} lowercase words.")

                numbers = []
                for word in words:
                    if word.isdigit():
                        numbers.append(int(word))
                number_count = len(numbers)
                print(f"There are {number_count} numeric strings.")

                suma = sum(numbers)
                print(f"The sum of all the numbers {suma}.")

                unsorted_occurence = {}
                for word in words:
                    if len(word) in unsorted_occurence.keys():
                        unsorted_occurence[len(word)] += 1
                    else:
                        unsorted_occurence[len(word)] = 1

                occurence = {}
                for key in sorted(unsorted_occurence.keys()):
                    occurence[key] = unsorted_occurence[key]

                print(separator)

                lenght = max(occurence.values()) + 1
                print("LEN|", "OCCURENCY".center(lenght), "|NR.")

                print(separator)

                for l, o in occurence.items():

                    if l < 10:
                        print(f"  {l}|", (o * "*").ljust(lenght), f"|{o}")
                    elif l >= 10:
                        print(f" {l}|", (o * "*").ljust(lenght), f"|{o}")


            else:
                print(f"{input_number} is not btw. 1 and 3", "terminating the program...", sep="\n")

        else:
            print(f"{input_number} is not a number", "terminating the program...", sep="\n")

    else:
        print("incorrect password, terminating the program..")

else:
    print("unregistered user, terminating the program..")

