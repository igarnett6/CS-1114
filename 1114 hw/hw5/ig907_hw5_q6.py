string = input("Please enter a string of lowercase letters: ");
def isIncreasing(string):
    for i in range(len(string)):
        currChar = string[i];
        if(i > 0):
            if(ord(currChar) < ord(string[i-1])):
                return False;
    return True;

if(isIncreasing(string)):
    print(string, "is increasing.");
else:
    print(string, "is not increasing.");





