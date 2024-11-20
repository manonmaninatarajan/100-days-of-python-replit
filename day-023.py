print("Replit Login System")
print()

def login():
  while True:
    uname=input("username:")
    passcode=input("password:")
    if uname=="david" and passcode=="baldies4life":
      print("Welcome to Replit!")
      exit()
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue


login()
    
