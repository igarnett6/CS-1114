side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))

if(side1 == side2 == side3):
    print(side1, ',', side2, ',', side3, "form an equilateral triangle")
elif(side1 == side2 or side1 == side3 or side2 == side3):
    print(side1, ',', side2, ',', side3, "form an isosceles triangle")