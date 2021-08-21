# This program generates and prints a Collatz sequence

from sys import exit

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        user_number = int(input('Enter a number (or enter 0 to exit)\n'))
        if user_number > 0:
            steps = 0
            altitude = user_number
            while user_number > 1:
                user_number = collatz(user_number)
                if user_number > altitude:
                    altitude = user_number
                steps += 1
                print(user_number)
            print('Sequence finished after ' + str(steps) + ' steps with a max altitude of ' + str(altitude), end='\n\n')
        else:
            exit()
    except ValueError:
        print('Oops! That\'s not a number!')

