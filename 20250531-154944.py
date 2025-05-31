Question 3__________
Write a loop that prompts the user
to enter a series of 
pizza toppings until they enter a 
'quit' value. As they enter each 
topping, 
print a message saying you’ll add
that topping to their pizza.
solution ________________
while True:
    topping = input("Enter a pizza 
    topping (or type 'quit' to stop): ")

    if topping.lower() == 'quit':
        print("Finished making your pizza!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
