expenses =[]
while True:
    amount =  float(input("expense Amount: "))

    expenses.append(amount)

    more = input("Add more ? yes/no")

    if more == "no":
        break 

print("Total spent : ",sum(expenses))