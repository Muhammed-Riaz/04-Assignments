# import random 

# def computer_guess():
#   high = 10
#   low = 1
#   feedback = ''
#   while feedback != 'c':
#     guess = random.randint(low,high) 
#     feedback = input(f"is {guess} to low (l) , to high (h) , correct (c)")
#     if feedback == 'l' :
#      low = guess+1  
#     elif feedback == 'h':
#       high = guess -1
#     elif feedback == 'c':
#       print(f"the computer guessed {guess} correctly") 
      

# computer_guess()




# import random

# def rock_paper_scissors():
#     choices = ["rock", "paper", "scissors"]
    
#     while True:
#         player = input("Enter Rock, Paper, or Scissors (or 'q' to quit): ").lower()
        
#         if player == 'q':  # Option to exit
#             print("Thanks for playing!")
#             break
        
#         if player not in choices:  # Check if input is valid
#             print("Invalid choice! Please choose Rock, Paper, or Scissors.")
#             continue
        
#         computer = random.choice(choices)  # Computer's random choice
#         print(f"Computer chose: {computer}")

#         # Determine the winner
#         if player == computer:
#             print("It's a tie!")
#         elif (player == "rock" and computer == "scissors") or \
#              (player == "scissors" and computer == "paper") or \
#              (player == "paper" and computer == "rock"):
#             print("You win!")
#         else:
#             print("You lose!")

# rock_paper_scissors()





import random 

def monitor_guess():

  choice = ["paper" ,"scissor" ,"rock"]
  while True :
    computer = random.choice(choice)
    user = input("Enter your choice (paper,rock,scissor) (or 'q' to exit)")

    if user == 'q':
     print("thanks for playing")
     break 
    if user not in choice:
      print("Invalid choice! Please choose rock, paper, or scissors.")
      continue
    if( user == 'paper' and  computer == "rock") or \
     (user == 'rock' and computer == "scissor") or \
     (user == 'scissor' and computer == "paper"):
      print(f"{computer} you won ")
    else : 
      print("You are lose go to home and cry")
    
monitor_guess()
