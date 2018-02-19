def encode(str):
    output = []
    count =1
    length = len(str)
    for i in range(1, length):
        sub = []
        if(str[i] == str[i-1]):
            count +=1
            saveCount = count
        else:
            sub.append(str[i-1])
            sub.append(count)
            output.append(sub)
            count = 1
    sub.append(str[i - 1])
    sub.append(count)
    output.append(sub)
    return output

def decode(lst):
    output = ""
    length = len(lst)
    for i in range(length):
        output += int(lst[i][1])*str(lst[i][0])
    return output

def main():
    string = "aadccccaa"
    cypher = encode(string)
    print("Encoded: ", cypher)
    decoded = decode(cypher)
    print("Decoded: ", decoded)

main()


