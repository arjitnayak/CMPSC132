import random
import math

def number_guessing_game():
    num = random.randint(1,100)
    guess = -math.inf
    attempts = []
    print("Welcome to the Single Player Number Guessing Game")
    print("Rules are Simple:")
    print("1. The Computer Generates a Random Number Between 1-100 (INCLUSIVE) and You Must Guess It")        
    print("2. Based On Your Input, The Computer Will Give You Feedback (\"Too High\" or \"Too Low\")")
    print("3. The Game Will End As Soon As You Get The Correct Number and Will Display The Number of Attempts It Took You")
    print("4. Last But Not Least, Have Fun\n")

if __name__ == "__main__":
    number_guessing_game()