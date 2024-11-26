import random,os,time

def rolldice(sides):
  result=random.randint(1,sides)
  return result
def health():
  health_stats=((rolldice(6)*rolldice(12))/2) +10
  return health_stats
def strength():
  strength=((rolldice(6)*rolldice(8))/2) +12
  return strength

while True:
  print()
  print(input("Name your legend: "))
  print(input("Character Type (Human, Elf, Wizard, Orc): "))
  print("Health:",health())
  print("Strength",strength(),"/n")
  print("May your name go down in Legend...")
  time.sleep(1)
  ans=input("Do you wanna play again? (yes/no):")
  if ans.islower() == "yes":
    continue
  else: 
     break 

os.system('clear')
