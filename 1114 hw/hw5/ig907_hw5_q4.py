userWord = input("Enter a word: ");
countVowel = 0;
countCons = 0;
for i in range(len(userWord)):
    currentChar = userWord[i];
    if(currentChar == 'a' or currentChar == 'e' or currentChar == 'i' or currentChar == 'o' or currentChar == 'u'):
        countVowel+=1;
    else:
        countCons+=1;
print(userWord, "has", countVowel, "vowels and",countCons,"consonants.");