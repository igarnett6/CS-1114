import math;
#startQuestion5
dob = int(input("Please enter a date of birth:"));
date = int(input("Please enter today's date:"));

year1 = int((dob-(dob % 10000))/10000);
year2 = int((date - (date % 10000))/10000);

totYears = total//365;
month1 = int(((dob % 10000)-(dob % 100))/100);
month2 = int(((date % 10000) - (date % 100))/100);
totalMonth = (total % 365)//30;

day1 = int((dob % 100));
day2 = int((date % 100));

total = (year2*365)+day

print(total);
print("year 1: ", year1);
print("year 2: ", year2);
print("month 1: ", month1);
print("month 2: ", month2);
print("day 1:", day1);
print("day 2: ", day2);
print("Total years:", totYears);
print("Total monthS: ", totalMonth);

