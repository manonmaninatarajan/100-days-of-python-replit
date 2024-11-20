print("Loan Caculator")
print()
loan_amount=int(input("Enter the loan amount: "))
interest_rate=int(input("Enter the intrest rate per year:"))
years=int(input("How many years do you want to borrow? "))
for i in range(years):
  loan_amount+=(loan_amount*interest_rate/100)
  print("Year",i+1,"is",round(loan_amount,2))
