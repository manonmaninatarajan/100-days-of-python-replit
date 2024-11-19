intrest=input("Whats your intrest?")
if intrest=="coding":
  print("You are a coder")
  language=input("what is you favourite language?")
  if language=="python":
    print("You are a python coder")
  elif language=="HTML":
    print("HTML is not considered a coding language, but it's essential for web development!")
  else:
    print("You are a" ,language,"coder")
else:
  print("You are not a coder")
