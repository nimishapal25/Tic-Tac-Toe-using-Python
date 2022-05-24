import random
# change
answer = random.randint(1, 10)
print(answer)
userInput = 0
while answer != userInput:
    userInput = int(input('Choose a number between 1 to 10: '))

    if userInput == answer:
        print('You guessed right')
    else:
        if answer > userInput:
            print('Guess Higher')
        else:
            print('Guess Lower')
