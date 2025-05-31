Question 4____________
A movie theater charges different
ticket prices depending on 
a person’s age. If a person is 
under the age of 3, the ticket is
free; if they are 
between 3 and 12, the ticket is
$10; and if they are over age 12,
the ticket is 
$15. Write a loop in which you ask
users their age, and then tell them
the cos

solution ________________________
while True:
    age_input = input("Enter your
    age to find out the ticket price (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Thank you for visiting the
        theater!")
        break
    else:
        age = int(age_input)

        if age < 3:
            print("The ticket is free!")
        elif age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
