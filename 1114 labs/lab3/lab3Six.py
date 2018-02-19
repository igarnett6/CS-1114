sides = int(input("Enter the number of sides: "));
if(sides == 3):
    print("The shape is triangle.")
elif(sides == 4):
  res =  input("Are the angles 90 degrees? (Y/N): ");
  if(res == "y"):
      res = input("Are the sides equal? (Y/N): ");
      if(res == "y"):
          print("The shape is square.");
      else:
          print("The shape is rectangle.");
  else:
          print("The shape is quadrilateral.");
elif(sides == 5):
    print("The shape is pentagon.");

