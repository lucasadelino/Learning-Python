# This program generates and prints a Collatz sequence

from sys import exit

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        user_number = altitude = int(input('Enter a number (or enter 0 to exit)\n'))
        if user_number > 0:
            steps = 0
            while user_number > 1:
                user_number = collatz(user_number)
                steps += 1
                if user_number > altitude:
                    altitude = user_number
                print(user_number)
            print('Sequence finished after ' + str(steps) + ' steps with an altitude of ' + str(altitude), end='\n\n')
        elif user_number < 0:
            print('Please enter a positive integer')
        else:
            exit()
    except ValueError:
        print('That\'s not a number.')

