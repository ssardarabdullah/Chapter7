while True:
    age_input = input("Enter your age to find out the ticket price (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Thank you for visiting the theater!")
        break
    else:
        age = int(age_input)

        if age < 3:
            print("The ticket is free!")
        elif age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")