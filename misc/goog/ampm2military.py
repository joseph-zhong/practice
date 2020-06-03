#!/usr/bin/env python3
# ampm2military.py
#

def convert(time):
    """
        Takes a time in AMPM format (e.g. 12:00am) and converts it to the equivalent military time (00:00)
    """
    assert time.count(':') == 1 and (time.endswith('am') or time.endswith('pm'))

    hrs, mins = time.split(':')
    hrs = int(hrs)
    period = mins[-2:]
    mins = int(mins[:-2])

    if hrs == 12:
        hrs += 12
    if period == 'pm':
        hrs += 12
    hrs %= 24

    return '{:02d}:{:02d}'.format(hrs, mins)

print(convert('12:00am') == '00:00')
print(convert('01:00am') == '01:00')
print(convert('02:00am') == '02:00')
print(convert('03:00am') == '03:00')
print(convert('04:00am') == '04:00')
print(convert('05:00am') == '05:00')
print(convert('06:00am') == '06:00')
print(convert('07:00am') == '07:00')
print(convert('08:00am') == '08:00')
print(convert('09:00am') == '09:00')
print(convert('10:00am') == '10:00')
print(convert('11:00am') == '11:00')
print(convert('12:00pm') == '12:00')

print(convert('01:00pm') == '13:00')
print(convert('02:00pm') == '14:00')
print(convert('03:00pm') == '15:00')
print(convert('04:00pm') == '16:00')
print(convert('05:00pm') == '17:00')
print(convert('06:00pm') == '18:00')
print(convert('07:00pm') == '19:00')
print(convert('08:00pm') == '20:00')
print(convert('09:00pm') == '21:00')
print(convert('10:00pm') == '22:00')
print(convert('11:00pm') == '23:00')
