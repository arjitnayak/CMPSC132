import random
import math

def number_guessing_game():
    print("\nGenerating Number...")
    num = random.randint(1,100)
    print("Number Generated\n")
    guess = -math.inf
    attempts = []
    while ((num != guess) and (len(attempts) < 5)):
        try:
            guess = int(input("What's Your Guess: "))
            if (guess > num):
                print("The Number Entered is Too High")
            elif (guess < num):
                print("The Number Entered is Too Low")
            attempts.append(guess)
        except ValueError:
            print("Please Enter an Integer")
    if (num != guess):
        print("\nYou Lost :(")
        print(f"The Number Was {num}")
    else:
        print(f"\nCongratulations! The Number Was {guess}")
        print(f"You Took {len(attempts)} Attempts To Guess The Correct Number\n")
        

if __name__ == "__main__":
    print("Welcome to the Single Player Number Guessing Game")
    print("Rules are Simple:")
    print("1. The Computer Generates a Random Number Between 1-100 (INCLUSIVE) and You Must Guess It In 5 Attempts")        
    print("2. Based On Your Input, The Computer Will Give You Feedback (\"Too High\" or \"Too Low\")")
    print("3. The Game Will End As Soon As You Get The Correct Number and Will Display The Number of Attempts It Took You")
    print("4. Last But Not Least, Have Fun\n")
    status = input("Do You Want To Play? (Y/N): ")
    while status == "Y":
        number_guessing_game()
        status = input("\nDo You Want To Play Another Round? (Y/N): ")
    print("\nThank You For Playing the Single Player Number Guessing Game")
    print("Make Sure To Come Back To Play More")