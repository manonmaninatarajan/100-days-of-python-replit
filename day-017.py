from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
count1=0
count2=0
while True:
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")  
  if count1==3 or count2==3:
    if count1>count2:
      print("Player 1 wins with",count1,"victories!")
      exit()
    elif count2>count1:
      print("Player 2 wins with",count2,"victories!")
      exit()
    else:
      print("It's a tie!")
      exit()
  if player1Move in ["R","P","S"] and player2Move in ["R","P","S"]:    
    if player1Move=="R":
      if player2Move=="R":
         print("You both picked Rock, draw!")
      elif player2Move=="S":
         print("Player1 smashed Player2's Scissors into dust")
         count1+=1

      elif player2Move=="P":
         print( "Player1's Rock is smothered by Player2's Paper!")  
         count2+=1

    elif player1Move=="P":
      if player2Move=="P":
         print("You both picked Paper, draw!")
      elif player2Move=="R":
         print("Player2's Rock is smothered by Player1's Paper!")
         count1+=1
      elif player2Move=="S":
         print( "Player1's Paper cut into pieces by Player2's Scissors!")
         count2+=1


    elif player1Move=="S":
      if player2Move=="S":
         print("You both picked Scissors, draw!")
      elif player2Move=="R":
         print("Player2 smashed Player1's Scissors into dust")
         count2+=1
      elif player2Move=="P":
         print( "Player1's scissor cut palyer2 Paper into pieces!")
         count1+=1
    
  else:
    print("Invalid Move try again")
    continue
    
