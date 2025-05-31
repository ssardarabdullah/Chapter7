Question 5______________
Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to
control how long the loop runs.
•	 Use a break statement to exit
the loop when the user enters a 
'quit' value.

solution ______
prompt = "Enter a pizza topping (enter 'quit' to stop): "
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"  Adding {topping} to your pizza.")
