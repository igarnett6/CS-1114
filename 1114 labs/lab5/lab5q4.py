import turtle
turtle = turtle.Turtle();
numSides = int(input("Please enter the  number of sides: "))

angle = 360/numSides
dist = int(100)

for i in range(numSides):
    turtle.fd(dist);
    turtle.lt(angle);