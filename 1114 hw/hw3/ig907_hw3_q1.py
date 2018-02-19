weight = float(input("Please enter weight in kilograms:"));
height = float(input("Please enter height in meters:"));
bmi = weight/(height**2);
if(bmi >= 30):
    print("Obese");
elif(bmi <= 29.9 and bmi >= 25):
    print("Overweight")
elif(bmi <= 24.9 and bmi >= 18.5):
    print("Normal")
elif(bmi < 18.5):
    print("Underweight")
print("BMI is: ", bmi);