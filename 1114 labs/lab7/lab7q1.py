import random;
n = int(input("Enter a number n: "));
output = '';
for k in range(n, -1, -1):
    output = '';
    for i in range(k):
        randNum = random.randint(0, 10);
        randNum = str(randNum);
        output += (randNum + " ");
    print('\n' + output, end = '');
for k in range(0, (n+1), 1):
    output = '';
    for i in range(k):
        randNum = random.randint(0, 10);
        randNum = str(randNum);
        output += (randNum + " ");
    print(output);