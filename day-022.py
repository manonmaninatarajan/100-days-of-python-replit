import random

print("Challenge day 18")
print()
variable=random.randint(1,10000000)
count=0;
while True:
  ans=int(input("What is your guess?"))
  if ans < variable:
    print("Too low")
    count+=1
  elif ans > variable:
    print("Too high")
    count+=1
  elif ans == variable:
    print("You got it,you took",count,"many times to gues the answer")
    break
