# Brian Giblin
# 9/28/23
# Sandwich Shop Assignment


# Get the sandwich type choice from user
sandwich_type = input("Which sandwich would you like? Cheese or Veggie special? ").lower()

if sandwich_type == "cheese":
    # Ask for cheese type
    cheese_type = input("Which cheese would you prefer? mozzarella 'm' or cheddar 'c'? ").lower()
    if cheese_type == "m":
        print("You've chosen a Cheese sandwich with mozzarella.")
    elif cheese_type == "c":
        print("You've chosen a Cheese sandwich with cheddar.")
    else:
        print(f"Sorry, we don't have {cheese_type} cheese choice today.")

elif sandwich_type == "veggie special":
    print("You've chosen a Veggie special sandwich.")

else:
    print(f"Sorry, we don't have {sandwich_type} choice today.")