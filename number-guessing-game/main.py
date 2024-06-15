from random import randint

maxGuess = 3
print("Welcome to the number guessing game.")
print(f"You have maximum {maxGuess} guesses.")

def getUserInput(param):
    try:
        inpt = int(input(f"{param}: "))
        return inpt
    except ValueError:
        print(f"Please provide a valid integer for {param}")
        getUserInput(param)

def game():
    print("\n\nPlease select a range.")
    minInpt = getUserInput("Minium")
    maxInpt = getUserInput("Maximum")

    while maxInpt < minInpt:
        print("Maximum must be greater than minimum")
        maxInpt = getUserInput("Maximum")

    randNum = randint(minInpt, maxInpt)
    remainingGuess = maxGuess

    while remainingGuess > 0:
        userGuess = getUserInput("Guess Number")
        remainingGuess -= 1

        if randNum == userGuess:
            print(f"You guessed the correct number in {maxGuess - remainingGuess} guesses.")
            break
        else:
            print(f"You guessed the wrong number. Guesses remaining {remainingGuess}")

    else:
        print(f"Oops. You lost. The correct number was {randNum}")


try:
    while True:
        game()
except KeyboardInterrupt:
    print("\n\nThanks for playing.")
    exit()