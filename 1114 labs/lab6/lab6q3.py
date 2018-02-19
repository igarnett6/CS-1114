s = input("Please enter a string s: ")
k = int(input("Please enter a number: "))
result = ''
for i in range(0, len(s), k*2):
    segmentToFlip = s[i:i+k]
    segmentToKeep = s[i+k:i+k+k]
    result += segmentToFlip[::-1] + segmentToKeep
print(result)