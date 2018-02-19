s = int(input("Please enter time in the 24 hour format: "));
timeM = (s%100)
timeH = (s//100);
print(timeM);
print(timeH);

if(timeH > 12):
    dayN = "pm";
else:
    dayN = "am";
if(timeH == 00):
    timeH = 12;
if(timeH > 12):
    timeH = timeH//12;
if(timeM < 10):
    timeM = "0" + str(timeM);
timeH = str(timeH);
timeM = str(timeM);

print(timeH+":"+timeM+" in 12 hr format is: "+timeH+":"+timeM+ dayN+".");