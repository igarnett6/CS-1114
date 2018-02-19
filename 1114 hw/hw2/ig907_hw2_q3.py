#convert the angle given to radians, solve for angle2 then convert back to degrees
import turtle;
import math;

side1 = float(input("Enter side length 1:"));
side2 = float(input("Enter side length 2:"));
angle1 = float(input("Enter angle between sides 1 and 2:"));
radAngle1 = math.radians(angle1);
side3 = math.sqrt((side1**2 + side2**2) - (2*side1*side2*math.cos(radAngle1)));
angle2 = math.acos((side1**2-side2**2-side3**2)/(-2*side2*side3));
angle2 = math.degrees(angle2);

#print(side3);
#print(angle2)

#start drawing image
turtle.fd(side1);
turtle.lt(180-angle1);
turtle.fd(side2);
turtle.lt(180-angle2);
turtle.fd(side3);
turtle.done();


