#!/usr/bin/env python
"""reducer.py"""

from __future__ import division
import sys

current_date = 736695
current_temp1 = None
current_temp2 = None

for line in sys.stdin:
    line = line.strip()
    date_string, temp_string = line.split('\t', 1)
    date = int(date_string)
    temp = int(temp_string)

    while current_date != date:
        if not (current_temp1 and current_temp2):
            print('-99')
        current_temp1 = None
        current_temp2 = None
        current_date += 1

    if current_temp1:
        if current_temp2:
            raise AssertionError('There are more than two temperatures for the following date: %s' % (current_date))

        current_temp2 = temp
        # Note: this method assumes that TMAX will always be greater than or equal to TMIN
        current_temp_diff = abs(current_temp1 - current_temp2) / 10
        print('%.1f' % (current_temp_diff))
    else:
        current_temp1 = temp

if not (current_temp1 and current_temp2):
    print('-99')
