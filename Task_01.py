length= float(input("Enter the length of Zander (cm) :"))
if length<42:
    print(f"Zander is {length} cm which is below the size limit(42cm). Please release to lake again")
else:
    print(f"Zander is {length} cm which met the size limit")