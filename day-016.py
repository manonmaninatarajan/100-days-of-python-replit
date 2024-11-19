print("Name the lyrics")
print()
count=0
while True:
  answer=input("Never going to ______ you up.")
  if answer == "give":    
    print(answer)
    count+=1
    print("Well done! It only took you",count, "attempts.")
    break
  else:
    print(answer)
    count+=1
    print("Nope, try again.")
    print()
    
   
