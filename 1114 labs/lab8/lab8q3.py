string = input("Enter a binary number: ")

def encodeBinary(string):
    count = 1
    for i in range(len(string)):
        current = string[i]
        prev = string[i-1]
        if((i > 0) and (current == prev)):
            count += 1
            #print("Count: ", count)

        if((i > 0) and (current != prev)):
            oneOrZero = prev
            print(count, oneOrZero, "'s")
            count = 1

        if(i == (len(string)-1)):
            print(count, current, "'s")

encodeBinary(string)