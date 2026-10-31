# System should generate a random number ,Users answer should match with the sytem to win 


# Step-by-step coding approach

#Step 1: Import the random module
import random

# # Step 2: Define the range
n = range(100)

# # Step 3: Generate random number
system = random.choice(n)

# # Step 4: Give 10 chances
for i in range(10):

#     # Step 5: Get user input
   user = int(input("Guess the number: "))

#     # Step 6: Check the answer
   if user == system:
        print("Hurray! You Won")
        break

   elif user > system:
        print("Your guess is too high")

   else:
        print("Your guess is too low")

# # Step 7: If all chances are over
else:
    print("You lost! Better luck next time")
    print("Correct number:", system)

# --------------------------------------------------------------------------------------- 
