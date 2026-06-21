year = (int(input("enter a year to know whether it is a leap year or not : ")))
if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif(year % 100 == 0):
    print(f"{year} is not a leap year.")
elif(year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Another way - 
year2 = int(input("enter a year"))
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")