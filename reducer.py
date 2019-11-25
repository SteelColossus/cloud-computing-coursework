#!/usr/bin/env python
"""reducer.py"""

# Required for Python 3 style division
from __future__ import division
import sys

# Set the current date to an initial value. This initial value is the proleptic Gregorian ordinal
# (https://docs.python.org/2/library/datetime.html#datetime.date.toordinal) of the date 2018-1-1.
current_date = 736695
current_temp1 = None
current_temp2 = None

# For each line given by the mapper (passed into standard input)
for line in sys.stdin:
    # Remove trailing whitespace and split by the tab character to get the date temperature key-value pair, making sure to convert them to integers
    line = line.strip()
    date_string, temp_string = line.split('\t', 1)
    date = int(date_string)
    temp = int(temp_string)

    # While the current date is not equal to the date from the key-value pair
    # i.e. the date from the key-value pair has moved onto a new date from the previous key-value pair
    while current_date != date:
        # If either of the current temperatures are not set, then output the default value (-99)
        # i.e. a date does not have two temperature readings for TMIN and TMAX
        if not (current_temp1 and current_temp2):
            print('-99')
        # Clear out the current temperatures and move onto the next day in the date
        current_temp1 = None
        current_temp2 = None
        current_date += 1

    # If there is already a current temperature, i.e. this is the second temperature of a TMIN and TMAX pair
    if current_temp1:
        # If there are already two temperatures, raise an error as this should not happen
        if current_temp2:
            raise AssertionError('There are more than two temperatures for the following date: %s' % (current_date))

        # Set the temperature of the key-value pair as the second temperature
        current_temp2 = temp
        # Calculate the temperature difference by taking the absolute difference between the two temperatures and dividing them by 10
        # Division by 10 happens to convert from tenths of degrees into whole degrees (making the value now a float)
        # Note: this method assumes that TMAX will always be greater than or equal to TMIN
        current_temp_diff = abs(current_temp1 - current_temp2) / 10
        # Output the temperature difference formatted to 1 d.p.
        print('%.1f' % (current_temp_diff))
    # Otherwise, just set the temperature of the key-value pair as the first temperature
    else:
        current_temp1 = temp

# If there is another default value (-99) that needs to be output after the loop, it is output here
if not (current_temp1 and current_temp2):
    print('-99')
