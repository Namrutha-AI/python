# Rock Paper Scissors Game

# n = ["Rock","Papers","Scissors"]
# for i in n:
#     print(i) 


# -----------------------------------------------------------------------------------------------------------------------------------



# # I want to get input from the user . If the user types Rock , they win.

# n = ["Rock","Papers","Scissors"]
# n1 = str(input())
# if n1 == "Scissors":
#    print("You Won")
# else:
#     print("The Answer is Scissors")

# --------------------------------------------------------------------------------------------------------------------------------------------

# User should be given 2 chances

# for i in  range(2):
#     n = str(input("Enter Rock ,paper or scissors"))
#     if n =="Rock":
#         print("Hurray!You Won")
#         break
#     else:
#         print("wrong guess,try again")
# else:
#         print("You lost,Better luck next time")

# ------------------------------------------------------------------------------------------------------------------------------------------------

# System should generate a random number ,Users answer should match with the sytem to win 


# Step-by-step coding approach

#Step 1: Import the random module
# import random

# # Step 2: Define the range
# n = range(100)

# # Step 3: Generate random number
# system = random.choice(n)

# # Step 4: Give 10 chances
# for i in range(10):

#     # Step 5: Get user input
#     user = int(input("Guess the number: "))

#     # Step 6: Check the answer
#     if user == system:
#         print("Hurray! You Won")
#         break

#     elif user > system:
#         print("Your guess is too high")

#     else:
#         print("Your guess is too low")

# # Step 7: If all chances are over
# else:
#     print("You lost! Better luck next time")
#     print("Correct number:", system)

# --------------------------------------------------------------------------------------- 


# The system generating a random answer in Rock ,paper,Scissors game
#Import the random module

import random 

#  Define a variable 
a =["Rock","Paper","Scissors"]

# Generate a random answer 
system =random.choice(a)

# Providing the chances

for i in range(2):
    user = str(input("Guess Rock ,Paper or Scissors:"))
    if user==system:
        print("Hurray ,You Won")
        break
    elif user !=system:
       print("Guess once again")

else :
    print("Sorry,You Lost")
    print("The answer is:",system)
