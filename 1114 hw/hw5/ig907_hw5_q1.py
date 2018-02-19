userInput = input("Enter an odd length string: ");

middleChar = userInput[int((len(userInput)/2))];
firstHalf = userInput[:(int(len(userInput)/2))];
secondHalf = userInput[int(len(userInput)/2):];

print("Middle charcter: ",middleChar);
print("First half: ",firstHalf);
print("Second half: ",secondHalf);
