import random
import time

def displayIntro():
    """Displays the intro to the game"""
    print("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight""")
    print()
    time.sleep(1)

def chooseCave():
    """Allows the user to select either cave 1 or cave 2"""
    cave = ""
    while cave != "1" and cave != "2":
        cave = input("Which cave will you enter? (1 or 2) ")
        if cave != "1" and cave != "2":
            print("Please enter \"1\" or \"2\"!")
            time.sleep(1)
    print()
    return int(cave)

def checkCave(chosenCave):
    """Checks whether or not the cave the user has selected is a winner"""
    print("You approach the cave...")
    time.sleep(1)
    print("It is dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)
    print()

    winner = random.randint(1, 2)
    if winner == chosenCave:
        print("Gives you all his treasure!")
    else:
        print("Gobbles you up in one bite!")

    print()
    time.sleep(1)
    


def game():
    displayIntro()

    playAgain = True
    playAgainChoice = ""


    while playAgain:
        chosenCave = chooseCave()
        checkCave(chosenCave)

        while True:
            playAgainChoice = input("Would you like to play again? ")
            if playAgainChoice.upper() in ["Y", "YES"]:
                playAgain = True
                break
            elif playAgainChoice.upper() in ["N", "NO"]:
                playAgain = False
            else:
                print("Please enter either \"Yes\" or \"No\"!")
                time.sleep(1)

game()

