myBill = float(input("What was the bill?: "))
tip=float(input("What percentage of tip would you like to give?"))
updated_bill=myBill+(myBill*tip/100)
numberOfPeople = int(input("How many people?: "))
answer = updated_bill / numberOfPeople
print("You all owe", answer)
