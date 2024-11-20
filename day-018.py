from getpass import getpass as input

print("Challenge day 18")
print()
variable=int(input("Pick a number between 0 and 1,000,000"))
count=0;
while True:
  ans=int(input("Pick a number between 0 and 1,000,"))
  if ans < variable:
    print("Too low")
    count+=1
  elif ans > variable:
    print("Too high")
    count+=1
  elif ans == variable:
    print("You got it,you took",count,"many times to gues the answer")
    break
  
    
