#!/usr/bin/evn python3

round = 0 #round initiated to 0
answer = " "

while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    
    round += 1 #increase round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______" ')
    answer = answer.capitalize()
    
    if answer == 'Brian': #logic to check if user gave correct answer
        print("Correct")

    elif answer == "Shrubbery":
        print("You gave the super secret answer!")

    elif round == 3:
        print("Sorry, the answer was Brian.") #logic to ensure round has not yet reached 3
    
    else:
        print("Sorry! Try again!") #if answer was wrong



