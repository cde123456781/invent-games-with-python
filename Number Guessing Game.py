import random

play_again = True

def generate_number():
    """Generates a number between 1 and 100"""
    return random.randint(1, 100)

def game():
    """Runs the full game with number generation, hints, and game conclusion"""
    number = generate_number()
    guesses = 0
    guess = 0
    while guess != number and guesses < 10:
        try:
            guess = int(input("Please guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter an integer between 1 and 100")
            else:
                guesses += 1
                if guess < number:
                    print("Your guess is less than the number")
                else:
                    print("Your guess is greater than the number")
        except:
            print("Please enter an integer")
    if guess != number:
        print("You failed to guess the number: {}".format(number))
    else:
        if guesses == 1:
            print("Congratulations! You guessed {} in 1 turn!".format(number))
        else:
            print("Congratulations! You guessed {} in {} turns!".format(number, guesses))

    



while play_again:
    # Call a function
    game()
    while True:

        play_again = input("Would you like to play again? ")
        if play_again.upper() in ["YES", "Y"]:
            play_again = True
            break
        elif play_again.upper() in ["NO", "N"]:
            play_again = False
            break
        else:
            print("Please enter \"Yes\" or \"No\"")


    