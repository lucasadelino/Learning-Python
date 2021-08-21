# This function takes a list of strings and prints those strings separated by commas, including an Oxford comma, if applicable

def commaprint(someList):
    if len(someList) == 0:
        print('Please give me a non-empty list')
    elif len(someList) == 1:
        print(str(someList[0]))
    elif len(someList) == 2:
        print(str(someList[0]) + ' and ' + str(someList[1])) # No comma between only 2 items
    else:
        for i in range(len(someList) - 1):
            print(str(someList[i]), end=', ')
        print('and ' + str(someList[-1]))


spam = ['apples', 'oranges', 'cats']

commaprint(spam) 