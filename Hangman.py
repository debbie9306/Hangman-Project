import random

countries = ["Austria", "Belgium", "Bulgaria", "Cyprus", "Czech Republic", "Denmark", "Germany", "Estonia", "Greece", "Spain", "Finland", "France", "Hungary", "Ireland", "Italy", "Croatia", "Lithuania", "Luxemburg", "Latvia", "Malta", "The Netherlands", "Poland", "Portugal", "Romania", "Sweden", "Slovenia", "Slovakia"]

answer = random.choice(countries).lower()
guessed_letters = []
#for illustration, reduced tries from 8 to 6
tries = 6
#added stages to illustrate hangman
stages = [
"""
  -----
  |   |
      |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
      |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
---------
""",
"""
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
---------
"""
]

print("Welcome to Hangman Game!")

while tries > 0:
    print(stages[6 - tries])
    
    display_word = ""

    for letter in answer:
        if letter == " ":
            display_word += " "
        elif letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    #To shoe which letter has been checked already
    print("Guessed letters:", " ".join(guessed_letters))

    if "_" not in display_word:
        print("You won! The word was:", answer.title())
        break

    guess = input("Guess a letter: ").lower().strip()

    if guess == "":
        print("Please enter a letter.")
        continue

    if guess in guessed_letters:
        print("You already tried that letter. Please enter a different letter.")
        continue

    guessed_letters.append(guess)

    if guess not in answer:
        tries -= 1
        print("That letter is not in the word. Tries left:", tries)

if tries == 0:
    #for the final illustration
    print(stages[6])
    print("You lost! The word was:", answer.title())
