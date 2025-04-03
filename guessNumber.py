# guess the number from 10 to 20

# generating a random number.
import random, sys
rnumber = random.randint(10, 20)

for x in range(6):
    print('Enter your guess(10-20):')
    guess = int(input())             #takes user input
    if 10 <= guess <= 20:
        if guess == rnumber :
            print(f'Your guess is correct. Its {guess}' )
            sys.exit()
        elif guess > rnumber :
            print('Your guess is high. Try again!!')
        elif guess < rnumber :
            print('Your guess is low. Try again!!')
    else:
        print('Enter your guess correctly(numeric from 10 to 20)')
print('Max try reached!!')        
