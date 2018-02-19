n = float(input("Enter the price of item one: "))
x = float(input("Enter the price of item two: "))
card  = input("Are you a card member (y/n)?: ")
price = float(x +n)
print("Price before deductions: ", price)
if(card == 'y'):
    member = 0;
else:
    member = 1;
if(x>=n):
    price = float(x + (n/2))
else:
    price = float((x/2)+n)
if(member == 0):
    price *= .9
else:
    price = price
print("The total price is: ", price)