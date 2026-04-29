import random
import math

def number_guessing_game(difficulty):
    print("\nGenerating Number...")
    num = random.randint(1,100)
    print("Number Generated\n")
    guess = -math.inf
    attempts = []
    attempts_num = {"e": 10, "m": 5, "h": 3}
    print(f"You Have {attempts_num[difficulty]} Attempts\n")
    while ((num != guess) and (len(attempts) < attempts_num[difficulty])):
        try:
            guess = int(input("What's Your Guess: "))
            if (guess > num):
                print("\nThe Number Entered is Too High")
            elif (guess < num):
                print("\nThe Number Entered is Too Low")
            attempts.append(guess)
        except ValueError:
            print("Please Enter an Integer\n")
        print(f"You Have {attempts_num[difficulty] - len(attempts)} Attempts Left\n")
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
    while(status not in status_levels):
        print("\nPlease Enter Y or N\n")
        status = input("Do You Want To Play? (Y/N): ").lower()
    while status == "y":
        difficulty = input("\nChoose Your Difficulty (E/M/H): ").lower()
        while(difficulty not in difficulty_levels):
            print("\nPlease Enter E or M or H\n")
            difficulty = input("Choose Your Difficulty (E/M/H): ").lower()
        number_guessing_game(difficulty)
        status = input("\nDo You Want To Play Another Round? (Y/N): ").lower()
        while(status not in status_levels):
            print("\nPlease Enter Y or N\n")
            status = input("Do You Want To Play? (Y/N): ").lower()
    print("\nThank You For Playing the Single Player Number Guessing Game")
    print("Make Sure To Come Back To Play More")