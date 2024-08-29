Cabin_Class=input("Enter the type of cabin class (LUX, A, B, C): ")
if Cabin_Class=="LUX":
    print("Upper-deck cabin with a balcony")
elif Cabin_Class=="A":
    print("Above the car deck, equipped with a window")
elif Cabin_Class=="B":
    print("Windowless cabin above the car deck")
elif Cabin_Class=="C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid Cabin Class")