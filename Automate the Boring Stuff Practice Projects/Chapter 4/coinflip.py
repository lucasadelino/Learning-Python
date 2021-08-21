# This program checks the (approximate) probability of getting a streak of (at least) 6 identical results in 100 coin tosses
import random
number_of_streaks = 0

for _ in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values, interpreted as 0 and 1
    resultList = [random.randint(0, 1) for _ in range(100)]

    # Code that checks if there is a streak of 6 'heads' or 'tails' in a row.
    streak = 1 #The minimum possible value for a streak is 1 (a single character).
    for i in range(99):
        if resultList[i] == resultList[i + 1]:
            streak += 1
        else:
            streak = 1
        if streak == 6:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 100))