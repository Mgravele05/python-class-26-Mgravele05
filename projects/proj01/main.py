# CS 31 Malachi Graveley, 10/23/2026

# Greet the customer and introduce your sales program.
print("Hello there, young trainer, Welcome to the wonderful world of Pokemon!"
      "\nA curious traveller like yourself can't go into wilderness without the latest Pokedex!"
      "\nIf you loan me a bit of your time, i'll show you why YOU must have one. ")
print()

# Ask the user if they would like to learn more about the product (If yes, give brief summary/If No, end progra with farewell)

learn_product = input("Does the Pokedex fancy your interest? (y/n): ")

if learn_product.lower() == "y":
    print("="*90)
    print('''Ah, step right up, you look like a trainer with big dreams! Tell me, 
how many times have you been out in the tall grass, spotted an incredible,
rare Pokémon, and thought, ‘What in the world is that?!’
    
Well, suffer no longer! Let me introduce you to the ultimate companion 
for your journey: The Pokédex!

Engineered by Professor Oak himself, this sleek, high-tech encyclopedia automatically 
identifies and logs data on every single species you encounter in the wild. Spot a Pikachu?
     
It'll give you its type, habitat, height, weight, and even its footprint! 
Catch it, and you'll unlock its full evolutionary history!
It’s durable, pocket-sized, and built to survive everything from burning deserts 
to freezing ice caves. 
    
Whether your goal is to conquer the Pokémon League or complete the world's most 
comprehensive field journal, you simply cannot leave Pallet Town without one.''')
    print("="*90)
    # Ask if they would like to purchase the product (If Yes, continue with the sale/If No, end the program, farewell)
    want_sale = input("Would you like to see the sale? (y/n): ")
    print()
    if want_sale.lower() == "y":
        # Making Sale: Ask for first/Last name, ask for Email and Phone number
        first_name = input("Fair traveler, who do I have the pleasure of speaking with?: ")
        last_name = input("And from which family do you hail? (Last name): ")
        full_name = f"{first_name} {last_name}"
        email = input("Now i must inquire on what email do you have?: ")
        phone = input("What number would be best to reach you?: ")
        print()

        # Tell the customer how much it cost


        print("The Pokedex will cost you 19.99$")
        print()

        # Ask them how many of the product they would like to buy
        amount_products = int(input("How many Pokedex would you like?: "))

        # Calculate and display the subtotal
        # Apply a 10% sales tax
        # Calculate and display the total amount

        pokedex = 19.99
        subtotal = amount_products * pokedex
        tax = subtotal * 0.10
        total = subtotal + tax

        # Create a receipt: display Customer name, Email and Number (Make it nicely formatted)
        # Quanity of items and how much per item
        # Subtotal, tax and total amount due

        print()
        print("="*30)
        print("       POKEDEX RECEIPT")
        print("="*30)
        print(f"Traveller: {full_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("=" * 30)
        print(f"Amount: {amount_products} Pokedex")
        print(f"Price per Item: {pokedex}")
        print("-"*30)
        print(f"Subtotal: {subtotal}")
        print(f"Tax (10%): {tax}")
        print("="*30)
        print(f"Total: {total}")
        print("="*30)

        # Give a Thank You and Farewell message
        
        print(f'''Congratulations on your new Pokédex!
        
May it guide you well on your journey through the tall grass,
take good care of your Pokémon, travel safely, and may your paths 
be filled with rare discoveries and unforgettable adventures!
 
Safe travels, {full_name}, and good luck filling up those pages!''')

    elif want_sale.lower() == "n":
        print("I don't understand you, traveller, Good luck on your journey!")
    else:
        print("invalid input")

elif learn_product.lower() == "n":
    print("\nNo hard feelings traveler, best of luck to you!")
else:
    print("\ninvalid input")