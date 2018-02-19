import math
a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))

posNeg = float(b**2-(4*a*c))
if(a == 0):
    print("No real solutions.")
elif(posNeg > 0):
    solution = (-b + math.sqrt(b**2-4*a*c))/2*a
    print("One solution at: x = ",solution)

else:
    solution = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("Two solutions at: x = -", abs(solution), " and x = ", abs(solution), sep = '')
