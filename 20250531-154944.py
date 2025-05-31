while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")

    if topping.lower() == 'quit':
        print("Finished making your pizza!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")