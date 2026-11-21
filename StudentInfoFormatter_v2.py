
# Student Information Formatter Version 2

first_name = input("Enter first name: ").strip().title()
last_name = input("Enter last name: ").strip().title()
section = input("Enter section: ").strip().upper()
favorite_subject = input("Enter favorite subject: ").strip().title()

full_name = first_name + " " + last_name

print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Favorite Subject:", favorite_subject)
print("Character Count:", len(full_name))
