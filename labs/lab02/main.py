# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Malachi Graveley 10/07/2026

# Output a title for the program. 
print("My AWESOME Quiz on pokemon!") # Title
print() # Space
print("*" * 20) # prints a line of 20 of the symbol

# Ask the user for their name. Greet them and use their name one more time in your output. 

print() # Space
Username = input("what's your name?: ") # User inputs their name
print(f"Hello, {Username}!") # use of F String and display user name

# Ask if the user would like to take a quiz. Depending on their answer - move to the questions or give a farewell greeting (maybe next time?).  

print() # Space
start_Quiz = input("Do you want to take my quiz? Y/N: ") # Asks user input
if start_Quiz.upper() == "Y": # If Statement & This will make any lowercase input into an uppercase
    print("Great, let's get started!") # Display for YES

# Initialize a variable that will be used as a counter that will store the total amount of correct answers. Set it to 0 at the beginning of the program.

    counter = 0

# Print out each quiz question with a question number. Example: 1) What is 5 + 5 ? 

    # Question 1 example for math
    print()
    q1 = int(input("How would Python solve 5 * 5?: "))
    if q1 == 25:
        print()
        print("You are correct, Good Job!")
        counter += 1
    else:
        print()
        print("Sorry. that was incorrect")

    # Question 2 Example for multiple choice
    print()
    print("What is the function that we use to output something to the terminal?")
    print()
    print(" A - Output()")
    print(" B - print()")
    print(" C - format()")
    print(" D - None of the above")
    print()
    q2 = input("Your answer - Choose A/B/C/D: ")
    if q2.upper() == "B":
        counter += 1
        print()
        print("Yes! you are correct")
    else:
        print()
        print("That's wrong Sir/Ma'am")

    # Question 3 

    # q3 = 



    # Output for result
    print()
    print("* * * YOUR FINAL SCORE * * * ")
    print()
    print(f"   Your final score is: {counter}")

    #Give them feedback on their overall score
    print()
    if counter == 5:
        print("You are a rockstar! you got them all right!")
    elif counter >= 3 and counter < 5:
        print("Great work!")
    elif counter >= 1 and counter < 3:
        print("Not the best score...")
    else:
        print("Sorry. you can't do this.")
    

# Create a variable to store the answer. Be very specific about what the user should type depending on the way you have setup your questions.
# Check to see if their answer is correct. If it is the correct, add 1 to the variable counter for a correct response. 
# Provide some feedback to let them know if their answer was correct or not. 
# Move on to questions 2 through 5, continuing to keep score. 
# When all of the questions have been completed, output their score. 
# Depending on their score, give them personalized feedback using an if/elif/else statement.
# Such as:
# 5/5 = Awesome work! You are a Rockstar.
# 4/5 = Nice job! Almost 100%.
# 2 or 3/5 = Keep studying!
# 0 or 1/5 = Maybe this isn't your area of interest? 
# Be sure to provide a farewell message. 
# Comment your code, test your code well, and have fun!



elif start_Quiz.upper() == "N": # Elif statement 
    print("Sorry, Maybe next time...") # Display for NO
else: 
    print("Sorry. That is an invalid response. try again")