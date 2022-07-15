import random

print("""██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██      
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██      
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ \n""")

print("""████████  ██████  
   ██    ██    ██ 
   ██    ██    ██ 
   ██    ██    ██ 
   ██     ██████ \n""")

print("""██████   ██████   ██████ ██   ██ 
██   ██ ██    ██ ██      ██  ██  
██████  ██    ██ ██      █████   
██   ██ ██    ██ ██      ██  ██  
██   ██  ██████   ██████ ██   ██ \n""")

print("""██████   █████  ██████  ███████ ██████  
██   ██ ██   ██ ██   ██ ██      ██   ██ 
██████  ███████ ██████  █████   ██████  
██      ██   ██ ██      ██      ██   ██ 
██      ██   ██ ██      ███████ ██   ██ \n""")

print("""███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
██      ██      ██ ██      ██      ██    ██ ██   ██ ██      
███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ 
     ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ 
███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ \n""")

gameon = input("Would you like to play?\n\nType 'y' or 'n': ")

while(gameon == "y"):
  
  rps = ["Rock", "Paper", "Scissors"]
  
  choose = input("\nWhat do you choose?\n\nType 0 for Rock, 1 for Paper or 2 for Scissors: ")
  
  playerchoice = rps[int(choose)]
  
  print(f"\nYou chose {playerchoice}!\n")
  
  randomchoice = rps[random.randint(0,2)]
  
  print(f"Opponent chose {randomchoice}!\n")
  
  if(playerchoice == rps[0] and randomchoice == rps[2]):
    print("""██     ██ ██ ███    ██ 
██     ██ ██ ████   ██ 
██  █  ██ ██ ██ ██  ██ 
██ ███ ██ ██ ██  ██ ██ 
 ███ ███  ██ ██   ████ 
\n""")
  if(playerchoice == rps[1] and randomchoice == rps[0]):
    
    print("""██     ██ ██ ███    ██ 
██     ██ ██ ████   ██ 
██  █  ██ ██ ██ ██  ██ 
██ ███ ██ ██ ██  ██ ██ 
 ███ ███  ██ ██   ████ 
\n""")
  if(playerchoice == rps[2] and randomchoice == rps[1]):
    
    print("""██     ██ ██ ███    ██ 
██     ██ ██ ████   ██ 
██  █  ██ ██ ██ ██  ██ 
██ ███ ██ ██ ██  ██ ██ 
 ███ ███  ██ ██   ████ 
\n""")
  if(playerchoice == rps[0] and randomchoice == rps[0]):
    print("""████████ ██ ███████ 
   ██    ██ ██      
   ██    ██ █████   
   ██    ██ ██      
   ██    ██ ███████ \n""")
  if(playerchoice == rps[1] and randomchoice == rps[1]):
    print("""████████ ██ ███████ 
   ██    ██ ██      
   ██    ██ █████   
   ██    ██ ██      
   ██    ██ ███████ \n""")
  if(playerchoice == rps[2] and randomchoice == rps[2]):
    print("""████████ ██ ███████ 
   ██    ██ ██      
   ██    ██ █████   
   ██    ██ ██      
   ██    ██ ███████ \n""")
  if(playerchoice == rps[0] and randomchoice == rps[1]):
    print("""██       ██████  ███████ ███████ 
██      ██    ██ ██      ██      
██      ██    ██ ███████ █████   
██      ██    ██      ██ ██      
███████  ██████  ███████ ███████\n""")
  if(playerchoice == rps[1] and randomchoice == rps[2]):
    print("""██       ██████  ███████ ███████ 
██      ██    ██ ██      ██      
██      ██    ██ ███████ █████   
██      ██    ██      ██ ██      
███████  ██████  ███████ ███████\n""")
  if(playerchoice == rps[2] and randomchoice == rps[0]):
    print("""██       ██████  ███████ ███████ 
██      ██    ██ ██      ██      
██      ██    ██ ███████ █████   
██      ██    ██      ██ ██      
███████  ██████  ███████ ███████\n""")
  gameon = input("Would you like to play again?\n\nType 'y' or 'n': ")
if(gameon == "n"):
  print("\nExiting...")