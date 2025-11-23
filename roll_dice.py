import random

roll = random.randint(1,6)
# print('The computer rolled a ', roll)
# print('The computer rolled a '+ str(roll))

userChoice = int(input('enter a number from 1-6?\n'))

if userChoice == roll:
    print('choice matched')
else:
    print('choice not matched. user choice - ',userChoice,' computer choice - ', roll)