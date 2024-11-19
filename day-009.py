birth_year=input("what is your birth year?")
int_birth_year=int(birth_year)
if isinstance(int_birth_year,int):
  if 1925 <= int_birth_year <= 1946:
    print("you are a traditionalist")
  elif 1947 <= int_birth_year <= 1964:
    print("you are a baby boomer")
  elif 1965 <= int_birth_year <= 1981:
    print("you are a generation x")
  elif 1982 <= int_birth_year <= 1995:
    print("you are a millenial")
  elif 1996 <= int_birth_year <= 2015:
    print("you are a generation z")
  else:
    print("you are not a human :)")
else:
  print("Please enter a number")
