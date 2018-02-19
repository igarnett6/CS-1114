import random
num = random.randint(1, 101)
high = 100
low = 1
guesses = int(input("Enter number of guesses: "))
print("I thought of a number between 1 and 100! Try to guess it.")
while(guesses > 0):
    guess = int(input())
    if (guesses == 0):
        break;
    elif(guess > num):
        high = guess
        print("Range[", low, ",", high, "] Wrong! My number is smaller. Guesses left: ", guesses, sep = '')
    elif(guess < num):
        low = guess
        print("Range[", low, ",", high, "] Wrong! My number is bigger. Guesses left: ", guesses, sep ='')
    else:
        print("Your guess is correct")
        break
    guesses -= 1
print("Out of guesses! My number is", num)