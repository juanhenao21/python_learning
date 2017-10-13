import random

print('---------------------------')
print('  Guess that number game')
print('---------------------------')
print()

the_number = random.randint(0,100)

guess_text = input('Gues a number between 0 and 100: ')

guess = int(guess_text)

print(the_number<guess)

if (guess < the_number):
    print('Too low')
elif (guess > the_number):
    print('Too high')
else:
    print('You win')