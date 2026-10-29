# Module file for lab 5 - nameformat.py

def hello_world():
    print("Hello, i'm Shadow the Hedgehog!")


def say_hello(first_name):
    """Definition: A simple function that takes a first_name input and says hello to that name"""
    print(f"Hello there {first_name}, I hope you're doing well today.")
    print()

def full_name(first_name, last_name):
    """Definition: A simple function that takes a first_name & last_name input and says hello to that name"""
    print(f"{first_name} {last_name}")
    print()


def last_name_first(first_name, last_name):
    """Definition: A simple function that takes a first_name & last_name input and says last name first then first name"""
    print(f"{last_name}, {first_name}")
    print()