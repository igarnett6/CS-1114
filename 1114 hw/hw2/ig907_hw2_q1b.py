weight = float(input("Please enter weight in pounds:"));
height = float(input("Please enter height in inches:"));
mWeight = weight*.453592;
mHeight = height*.0254;
bmi = mWeight/(mHeight**2);
print("BMI is: ", bmi);
