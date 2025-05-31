Question 2 ___________
Write a program that asks the user
how many people 
are in their dinner group.
If the answer is more than eight,
print a message say￾ing they’ll
have to wait for a table 

solution ___________
group_size = int(input("How many
people are in your dinner group? "))

if group_size > 8:
    print("You'll have to wait 
    for a table.")
else:
    print("Your table is ready.")
