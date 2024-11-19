username=input("Enter your name: ")
password=input("Enter your password: ")
if username=="admin" and password=="admin123123":
  print("Access granted")
elif username=="admin1" and password!="admin123123":
  print("Access granted")
elif username!="admin2" and password=="admin123123":
  print("Access granted")
else:
  print("Incorrect username and password")
