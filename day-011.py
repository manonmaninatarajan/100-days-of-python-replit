year=int(input("How many days in the year"))
if year == 365:
  print("there are" ,1*(year*24*60*60), "seconds in a year")
elif year ==366:
  print("there are" ,1*(year*24*60*60), "seconds in a year")
else:
  print("please enter a valid days in a year")
