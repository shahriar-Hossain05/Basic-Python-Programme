import random
options = ["rock", "paper", "scissors"]
bot = random.choice(options)

player = input("Input your move(rock, paper, scissors): ")
print(f"Player: {player}")
print(f"Bot: {bot}")

if player == bot :
   print("Draw")

elif player == "rock":
   if  bot == "scissors":
      print("You Win")  
   else:
      print("(You Lost)")

elif player == "paper":
   if  bot == "rock":
      print("You Win")  
   else:
      print("(You Lost)")  

elif player == "scissors":
   if  bot == "paper":
      print("You Win")  
   else:
      print("(You Lost)") 

else:
   print("Please, input your move(rock, paper, scissors) correctly!!")                 