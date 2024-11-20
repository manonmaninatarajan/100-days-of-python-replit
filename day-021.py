number=int(input("Name your multiples:"))
score=0
for i in range(1,11): 
  print(i,"x",number,"=")  
  answer=input("") 
  if answer.isdigit():
    if int(answer)==i*number:
      print("Great work!")
      score+=1
    else:
      print("Nope. The answer was",i*number)
      continue
  else:
    exit()
print("You scored",score,"out of 10")
  
