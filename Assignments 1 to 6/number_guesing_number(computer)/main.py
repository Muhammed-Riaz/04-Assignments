import random 

def computer_guess():
  high = 10
  low = 1
  feedback = ''
  while feedback != 'c':
    guess = random.randint(low,high) 
    feedback = input(f"is {guess} to low (l) , to high (h) , correct (c)")
    if feedback == 'l' :
     low = guess+1  
    elif feedback == 'h':
      high = guess -1
    elif feedback == 'c':
      print(f"the computer guessed {guess} correctly") 
      

computer_guess()
