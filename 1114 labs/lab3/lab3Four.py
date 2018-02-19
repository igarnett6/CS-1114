a = float(input("Please enter a:"));
b = float(input("Please enter b: "));


#infinite solutions
if(b == 0 and a == 0):
    print("There are infinitely many solutions");
#no solution
elif(a == 0):
    print("The equation has no solution.");
#one solution
else:
    x = -b / a;
    print("The equation has a single solution and x =", x);
