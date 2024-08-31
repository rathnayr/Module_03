Year=int(input("Enter an year: "))
if (Year%4==0 and Year%100!=0) or (Year%400==0):
    print(f"{Year} is a Leap year")
else:
    print(f"{Year} is not a Leap year")


