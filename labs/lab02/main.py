# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Malachi Graveley 10/07/2026

# Output a title for the program. 
print("/\\/\\/\\/\\/\\/\\/\\" * 2)
print()
print("   The BEST Pokemon Quiz!") # Title
print() 
print("\\/\\/\\/\\/\\/\\/\\/" * 2)
print()
print("=" * 30)

# Ask the user for their name. Greet them and use their name one more time in your output. 

print()
Username = input("what's your name?: ")
print(f"Hello, {Username}!") # use of F String and display user name

# Ask if the user would like to take a quiz. Depending on their answer - move to the questions or give a farewell greeting (maybe next time?).  

print() 
start_Quiz = input("Do you want to take my quiz? Y/N: ") 
if start_Quiz.upper() == "Y": 
    print("Great, let's get started!")

    print()
    print("=" * 30)

# Initialize a variable that will be used as a counter that will store the total amount of correct answers. Set it to 0 at the beginning of the program.

    counter = 0

# Print out each quiz question with a question number. Example: 1) What is 5 + 5 ? 

    # Question 1
    print()
    print("Q1. Who is the mascot for Pokemon?")
    print()
    print(" A - Pikachu")
    print(" B - Lucario ")
    print(" C - Rowlet")
    print(" D - Mewtwo")
    print()
    q1 = input("Your answer - Choose A/B/C/D: ")
    if q1.upper() == "A":
        counter += 1
        print()
        print("You're off to a great start!")
    else:
        print()
        print("That's wrong Sir/Ma'am")
    

    # Question 2
    print()
    print()
    print("Q2. Who's the starter grass-type pokemon in Gen 1(Kanto)?")
    print()
    print(" A - Clefairy")
    print(" B - Togepi")
    print(" C - Meowth")
    print(" D - Bulbasaur")
    print()
    q2 = input("Your answer - Choose A/B/C/D: ")
    if q2.upper() == "D":
        counter += 1
        print()
        print("Someone knows their stuff, Next question!")
    else:
        print()
        print("That's wrong Sir/Ma'am")

    # Question 3 

    print()
    print()
    print("Q3. How many generations are there?")
    print()
    print(" A - 6 Generations")
    print(" B - 9 Generations")
    print(" C - 1 Generation")
    print(" D - 7 Generations")
    print()
    q3 = input("Your answer - Choose A/B/C/D: ")
    if q3.upper() == "B":
        counter += 1
        print()
        print("You're on route to bikng the greatest!")
    else:
        print()
        print("That's wrong Sir/Ma'am")

    # Question 4

    print()
    print()
    print("Q4. What Pokemon does charmander Evolve into?")
    print()
    print(" A - Greninja")
    print(" B - Mew")
    print(" C - Oshawatt")
    print(" D - Charizard")
    print()
    q4 = input("Your answer - Choose A/B/C/D: ")
    if q4.upper() == "D":
        counter += 1
        print()
        print("I'm impressed honestly, amazing job!")
    else:
        print()
        print("That's wrong Sir/Ma'am")

    # Question 5

    print()
    print()
    print("Q5. Which one of these pokemon is NOT an eevee Evolution?")
    print()
    print(" A - Ditto")
    print(" B - Vapereon")
    print(" C - Jolteon")
    print(" D - Leafeon")
    print()
    q5 = input("Your answer - Choose A/B/C/D: ")
    if q5.upper() == "A":
        counter += 1
        print()
        print("Rock on trainer!")
    else:
        print()
        print("That's wrong Sir/Ma'am")

    print()
    print()
    print("=" * 30)

    # Output for result

    print()
    print("* * * YOUR FINAL SCORE * * * ")
    print()
    print(f"   Your final score is: {counter}")
    print()
    print("=" * 30)

    # Give them feedback on their overall score

    print()
    if counter == 5:
        print("You're on fire traveler! you got them all right!")
    elif counter >= 3 and counter < 5:
        print("good job trainer! you did pretty well!")
    elif counter >= 1 and counter < 3:
        print("Not the best score...")
    else:
        print("Sorry... Maybe Digimon is your thing.")

    print(f"Thank you for playing my Quiz {Username}!")
    print()
    print("=" * 30)


elif start_Quiz.upper() == "N": # Elif statement 
    print("Sorry, Maybe next time...") # Display for NO
else: 
    print("Sorry. That is an invalid response. try again")

    