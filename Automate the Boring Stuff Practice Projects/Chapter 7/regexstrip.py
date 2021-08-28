# A regex version of the strip() method

import re

def regexstrip(some_string, arg = '\s'):
    strip = re.compile('^' + arg + '*|' + arg + '*$')
    return strip.sub('', some_string)

print(regexstrip('AAAbruceAAA'))