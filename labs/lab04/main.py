# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
# CS 31 Malachi Graveley, 10/21/2026

# Be sure to use functions as the starting program does.

import random

LIMIT = 10

def display_title():
    print("Guess the number game")
    print()

def play_game():
    print("""
E:  Easy - Guess from 1 - 10, limit 5 attempts 
M:  Medium - Guess from 1 - 100, limit 7 attempts 
H:  Hard - uess from 1 - 1000, limit 10 attempts 
        """)
    your_level = input("Which level would you like to play? E/M/H: ")
    if your_level.upper() == "E":
        LIMIT = 10
        attempts = 5
    elif your_level.upper() == "M":
        LIMIT = 100
        attempts = 7
    elif your_level.upper() == "H":
        LIMIT = 1000
        attempts = 10
    else:
        LIMIT = 1000000
        attempts = 2

    secret_number = random.randint(1, LIMIT)
    print(f"I am thinking of a number from  1 to {LIMIT}\n")
    counter = 1 # keep track of the total number of attempts

    # check if they gave any attempts left

    while (guess := int(input("Your guess: "))) != secret_number:
        # Check if they have any attempts left
        if counter > attempts:
            print("Sorry. you lose, no more attempts.")
            break
        # the guess is incorrect
        if guess < secret_number:
            print("Sorry your guess is too low\n")
        elif guess > secret_number:
            print("Sorry, your guess is too high\n")
        counter += 1 # Increment the guess attempt counter
    else:
        # if they guess it correctly
        print(f"\nCongrats! You guessed it in {counter} tries!\n")

def main():
    # The main program driver
    display_title()

    # Ask for the player's name

    player_name = input("Hi there, What is your name?: ")
    print()

    again = "y" # set initial game loop variable

    while again.lower() == "y": # play the game
        play_game()
        print()
        again = input(f"{player_name}, Would you like to play another game? (y/n):")
        print()

    print("Thanks for playing the game!")

    # If started as the main module, call the main() function
if __name__ == "__main__":
    main() 