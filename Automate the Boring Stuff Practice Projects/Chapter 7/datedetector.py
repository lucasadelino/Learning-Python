#Program to check whether a given date is valid. Date must match this format: DD/MM/YYYY

import re

date_regex = re.compile(r'([0-2]\d|30|31)/(0[1-9]|1[0-2])/((1|2)\d{3})')
months30 = ('04', '06', '09', '11')

def isleap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
        
def isvalid_date(date):
    mo = date_regex.search(date)
    if mo is None:
        print('Invalid: Date format must be DD/MM/YYYY')
        return False
    day, month, year, _ = mo.groups()
    if int(day) > 29 and month == '02' and isleap(int(year)):
        print('Invalid: February has 29 days in leap years')
        return False
    elif int(day) > 28 and month == '02' and not isleap(int(year)):
        print('Invalid: February has 28 days in non-leap years')
        return False
    elif int(day) > 30 and month in months30:
        print('Invalid: This month has 30 days')
        return False
    elif int(day) > 31 and month not in months30:
        print('Invalid: This month has 31 days')
        return False
    else:
        print('Valid')
        return True

isvalid_date('29/02/2024')