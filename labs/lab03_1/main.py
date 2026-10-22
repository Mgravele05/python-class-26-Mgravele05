# Starting file for LAB 3-1
# Include your course number, student first and last name, and date in the comment header

# display a Welcome message
print("The Miles Per Gallon program")
print()
rerun_Program = "y"

while rerun_Program.lower() == "y":

# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gallon_Cost = float(input("Enter Cost of gas:           "))


    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif gallon_Cost <= 0:
        print("Cost of gas must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        cpg = round(gallons_used/gallon_Cost, 2)
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Amount of Gallons used:    ",gallons_used)
        print("Cost per Gallon:           ",cpg)
        print()

        rerun_Program = input("Want to do another entry(y/n)?:   ")

print()
print("Bye!")
