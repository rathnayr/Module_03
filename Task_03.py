Gender= print("Enter the Biological Gender as (Male or Female): ")
Hemoglobin= float(input("Enter the Hemoglobin in g/l: "))

if Gender== "Male":
    if Hemoglobin<134:
        print(f"You are a {Gender} & your Hemoglobin level is low")
    elif 134<=Hemoglobin<=167:
        print(f"You are a {Gender} & your Hemoglobin level is normal")
    else:
        print(f"You are a {Gender} & your Hemoglobin level is high")
elif Gender== "Female":
    if Hemoglobin<117:
        print(f"You are a {Gender} & your Hemoglobin level is low")
    elif 117<=Hemoglobin<=155:
        print(f"You are a {Gender} & your Hemoglobin level is normal")
    else:
        print(f"You are a {Gender} & your Hemoglobin level is high")
else:
    print("You have entered incorrect Gender")

