import random
import math

def number_guessing_game(difficulty):
    print("\nGenerating Number...")
    num = random.randint(1,100) # randomly generate the target number between 1 and 100
    print("Number Generated\n")
    guess = -math.inf
    attempts = []
    attempts_num = {"e": 10, "m": 5, "h": 3} # map difficulty to allowed attempts
    print(f"You Have {attempts_num[difficulty]} Attempts\n")
    # loop until correct guess OR attempts run out
    while ((num != guess) and (len(attempts) < attempts_num[difficulty])):
        try:
            guess = int(input("What's Your Guess: ")) # convert user input to integer
            if (guess > num):
                print("\nThe Number Entered is Too High")
            elif (guess < num):
                print("\nThe Number Entered is Too Low")
            attempts.append(guess) # track all guesses to count attempts
        except ValueError:
            print("Please Enter an Integer\n") # handle non-integer input safely
        print(f"You Have {attempts_num[difficulty] - len(attempts)} Attempts Left\n")
    # check win/loss after loop ends
    if (num != guess):
        print("\nYou Lost :(")
        print(f"The Number Was {num}")
    else:
        print(f"\nCongratulations! The Number Was {guess}")
        print(f"You Took {len(attempts)} Attempts To Guess The Correct Number")
        

if __name__ == "__main__":
    print("Welcome to the Single Player Number Guessing Game")
    print("Rules are Simple:")
    print("1. The Computer Generates a Random Number Between 1-100 (INCLUSIVE) and You Must Guess It In A Certain Number of Attempts")   
    print("2. Easy (E) is in 10 Attempts, Medium (M) is in 5 Attempts, Hard (H) is in 3 Attempts")     
    print("3. Based On Your Input, The Computer Will Give You Feedback (\"Too High\" or \"Too Low\")")
    print("4. The Game Will End As Soon As You Get The Correct Number and Will Display The Number of Attempts It Took You")
    print("5. Last But Not Least, Have Fun\n")
    status_levels = ["y", "n"]
    difficulty_levels = ["e", "m", "h"]
    status = input("Do You Want To Play? (Y/N): ").lower()
    # validate user input for starting the game
    while(status not in status_levels):
        print("\nPlease Enter Y or N\n")
        status = input("Do You Want To Play? (Y/N): ").lower()
    # main game loop (runs multiple rounds)
    while status == "y":
        difficulty = input("\nChoose Your Difficulty (E/M/H): ").lower()
        # validate difficulty selection
        while(difficulty not in difficulty_levels):
            print("\nPlease Enter E or M or H\n")
            difficulty = input("Choose Your Difficulty (E/M/H): ").lower()
        number_guessing_game(difficulty)
        status = input("\nDo You Want To Play Another Round? (Y/N): ").lower()
        # validate replay input
        while(status not in status_levels):
            print("\nPlease Enter Y or N\n")
            status = input("Do You Want To Play? (Y/N): ").lower()
    print("\nThank You For Playing the Single Player Number Guessing Game")
    print("Make Sure To Come Back To Play More")