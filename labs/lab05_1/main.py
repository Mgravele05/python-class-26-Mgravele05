# Starting file for LAB 5-1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Malachi Grvaeley, 10/28/2026

import nameformat

def main():
    # program title
    print("---Name Organization Program---")

    # ask for first/last name
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")



    # menu system
    while True:
        print("=== MENU ===")
        print("""    1 - Say Hello
    2 - Output Full Name
    3 - Output Last Name, First Name
    4 - Read Module  Documentation
    5 - Exit Program""")

        menu_choice = input("What would you like to do?: ")

        # if  else block based on choice input

        if menu_choice == "1":
            # call say_hello
            nameformat.say_hello(first_name)
        elif menu_choice == "2":
            #call full_name
            nameformat.full_name(first_name, last_name)
        elif menu_choice == "3":
            # call last_name_first
            nameformat.last_name_first(first_name, last_name)
        elif menu_choice == "4":
            print("Documentation")
            help(nameformat.say_hello)
            help(nameformat.last_name_first)
        elif menu_choice == "5":
            print('Thank you for using my program')
            break
        else:
            print("Sorry, Invaild Input, try again.")

if __name__ == "__main__":
    main()