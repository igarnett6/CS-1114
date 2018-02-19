def getFirstWord(phrase):
    end = phrase.find(" ")
    output = phrase[:end]
    return output

def getNumWords(phrase):
    count = 0
    newPhrase = phrase
    while(newPhrase.find(" ") > 0):
        count+=1
        newPhrase = noFirstWord(newPhrase)
    output = count+1
    return output

def noFirstWord(phrase):
    start = phrase.find(" ") + 1
    output = phrase[start:]
    return output

def reverse(phrase):
    numWords = getNumWords(phrase)
    listWords = [getFirstWord(phrase)]
    newPhrase = phrase
    output = ""
    for i in range(1, numWords):
        newPhrase = noFirstWord(newPhrase)
        listWords.append(getFirstWord(newPhrase))
    newList = listWords[len(listWords)+1:0:-1]
    newList.append(listWords[0])
    for j in range(numWords):
        output += (newList[j]+" ")
    return output

def main():
    phrase = input("Enter a phrase: ")
    print("Original: ", phrase)
    print("Reversed: ", reverse(phrase))

main()
