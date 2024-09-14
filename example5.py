Weight = int(input("Weight: "))

Weight1 = str(input("lbs or Kg "))
if Weight1.upper == "L" :
     converted = Weight * 0.45
     print(f"Your are {converted} kgs")

else :
    converted = Weight / 0.45
    print(f"Your are {converted} lbs")






