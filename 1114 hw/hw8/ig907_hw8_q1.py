import math
import os
import random
def create_permutation(n):
    output = []
    while(len(output)<n):
        randVal = random.randint(0, (n-1))
        if(output.count(randVal)==0):
            output.append(randVal)
    return output

def scramble_word(word):
    n = len(word)
    order = create_permutation(n)
    newWord = ""
    for i in range(n):
        newWord += " " + word[order[i]]
    return newWord

def main():
   filename = "hw8 - word bank.txt"
   file = open(filename, "r")
   listOfWords = [file.readline()]
   for line in file:
       listOfWords.append(file.readline())
       numOfWords = len(listOfWords)
   randNum = random.randint(1,(numOfWords+1))
   currentAnswer = listOfWords[randNum]
   scrambled = scramble_word(currentAnswer)
   print("Unscramble the word: ", scrambled)
   for j in range(3):
       attempt = (j + 1)
       print("\nTry# ", attempt, ":", sep="", end="")
       userResponse = input() + "\n"
       if (currentAnswer == userResponse):
           print("Yay you got it!")
           break  # we won't talk about this...
       elif (j == 3):
           print("Wrong! Out of tries!")
       else:
           print("Wrong!")

main()
