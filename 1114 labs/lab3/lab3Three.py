name = input("Please enter your name: ");
gyear = input("Please enter your graduation year: ");
cyear = input("Please enter current year: ");

if(gyear < cyear):
    print(name, "has graduated.");
elif((gyear - cyear) == 4):
    print(name, "is a freshman.");
elif((gyeaer - cyear) == 3):
    print(name, "is a sophmore.");
elif((gyear-cyear) == 2):
    print(name, "is a junior.");
else:
    print(name, "is a senior.");
