print("Please select your ride:")
print("1. Bike")
print("2. Car")
choice=int(input("Please enter your choice here (1 or 2):"))
if choice == 1:
    print("Please select the colour:")
    print("1. Red")
    print("2. Blue")
    colour_choice=int(input("Please enter your choice here (1 or 2):"))
    if colour_choice == 1:
        print("Your customised ride is a red bike")
    else:
        print("Your customised ride is a blue bike")
else:
    print("Please select the colour:")
    print("1. Red")
    print("2. Blue")
    colour_choice=int(input("Please enter your choice here (1 or 2):"))
    if colour_choice == 1:
        print("Your customised ride is a red car")
    else:
        print("Your customised ride is a blue car")