userNumber = input("Enter a number to convert to text: ");
userInt = int(userNumber);
def convert(numToChange):
    return chr(numToChange);

numToUse = 500;
revOutput = '';
while(userInt != 0):
    numToUse = int(userInt%100);
    revOutput += convert(numToUse);
    userInt = userInt//100;

output = '';
for i in range((len(revOutput)-1), -1, -1):
    output += revOutput[i];
print(output);