jDays = int(input("Please enter the number of days John has worked:"));
jHours = int(input("Please enter the number of hours John has worked:"));
jMin = int(input("Please enter the number of minutes John has worked:"));
bDays = int(input("Please enter the number of days Bill has worked:"));
bHours = int(input("Please enter the number of hours Bill has worked:"));
bMin = int(input("Please enter the number of minutes Bill has worked:"));

coDays = jDays + bDays;
coHours = jHours + bHours;
coMin = jMin + bMin;

totMin = (coDays*24*60) + (coHours*60) + coMin;
totDays = totMin//1440;*2*//222222222222222222222222222222222222222222222222222222222222222222222
totMin = totMin%1440;
totHours = (totMin//60);
totMin = (totMin%60);


print("The total time both of them worked together is:", totDays, "days", totHours,"hours and", totMin,"minutes");2