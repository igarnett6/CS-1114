import math;



#startQuestion1
radius = int(input("Input an integer as the radius:"));
circumference = 2*math.pi*radius;
area = math.pi*radius**2
print("The circumference is %.2f" % circumference, "the area is %.2f" % area);
#endQuestion1

#startQuestion3
nod = int(input("Enter the number of days: "));
weeks = nod//7;
days = nod%7
print(nod, "is equal to ", weeks, "and", days);
#endQueston3

#startQuestion4
num = int(input("Enter a decimal integer less than 100."));
numL = num//50;
temp = num-numL;
numX = temp//10;
temp = temp-numX;
numV = temp//5;
temp = temp-numV;
numI = temp%5;
print(num, "in Roman Numeral is: ");
#endQuestion4

#startQuestion5
dob = input("Please enter a date of birth:");
date = input("Please enter today's date:")

year = dob-(dob % 1000);
print(year);




