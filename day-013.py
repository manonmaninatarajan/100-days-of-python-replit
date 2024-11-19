test_name=input("Can you please enter the name of you test:")
max_score=int(input("Can you please enter the maximum score you can receive:"))
actual_score=int(input("Can you please enter the actual score you received:"))
percentage=round(actual_score/max_score*100,2)
if 90<=percentage<=100:
  print(f"You got {percentage}% which is an A+")
elif 80<=percentage<=89:
  print(f"You got {percentage}% which is an A")
elif 70<=percentage<=79:
  print(f"You got {percentage}% which is a B")
elif 60<=percentage<=69:
  print(f"You got {percentage}% which is a C")
elif 50<=percentage<=59:
  print(f"You got {percentage}% which is a D")
elif percentage<50:
  print(f"You got {percentage}% which is a U")
else:
  print("Please enter a valid score in numbers")
