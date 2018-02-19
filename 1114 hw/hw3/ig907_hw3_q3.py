time = int(input("What hour is it?(24 hr format): "))
minutes = int(input("Enter the length of the call in minutes: "))
day = input("What day is it?: ")
if(day == "Sat" or day == "Sun"):
    day = 'y'
price = float(0)
if(day != 'y'):
    if(8 < time <18):
        price = .4*minutes
    else:
        price = .25*minutes
else:
    price = .15*minutes

print("The cost of the call is: $",price)