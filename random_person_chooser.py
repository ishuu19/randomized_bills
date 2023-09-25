# paying bill randomized


import random

mylist = str(input("Please enter the names with a comma:"))

updated_names = mylist.split(", " or ",")
choice = len(updated_names)

up_choice = random.randint(0, choice-1)
payer = updated_names[up_choice]

print(f"{payer.capitalize()} will pay the bill.")