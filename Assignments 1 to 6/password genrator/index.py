import random 
import string

def genrate_password(length=20):

  print("""Genrated rendom password is: """)

  if length < 4:
    raise ValueError
  
  all_char = string.ascii_letters + string.digits + "!@#%^&*"

  password = random.sample(all_char,length)
   
  return "".join(password)

try:
 user_input = int(input("Enter a number :"))
 print(genrate_password(user_input))
  
except ValueError:
 print("Incorrect number")
  
