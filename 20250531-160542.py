prompt = "Enter a pizza topping (enter 'quit' to stop): "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"  Adding {topping} to your pizza.")