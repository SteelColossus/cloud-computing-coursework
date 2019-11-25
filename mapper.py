#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime

# The ID of the weather station / location to gather values for.
# Can either be UK000056225 (Oxford) or UK000003377 (Waddington).
station_id_to_capture = 'UK000056225'

# For each line in the input CSV file (passed into standard input)
for line in sys.stdin:
    # Remove trailing whitespace and split by commas into individual fields
    line = line.strip()
    fields = line.split(',')
    # Give names to the important fields so that they are more human readable
    station_id = fields[0]
    measure = fields[2]
    quality = fields[5]

    # We only want to send this line to the reducer if:
    #   The location is the same as the one above
    #   The measurement is either a TMAX measurement or TMIN measurement
    #   The measurement hasn't failed any quality checks (i.e. the quality flag is blank)
    if station_id == station_id_to_capture and (measure == 'TMAX' or measure == 'TMIN') and quality == '':
        # Get the date of the measurement. The date is parsed and then converted into a proleptic Gregorian ordinal
        # (https://docs.python.org/2/library/datetime.html#datetime.date.toordinal), effectively an integer representing the date.
        # This is done because it is easier to work with than date strings.
        date_string = fields[1]
        date = datetime.strptime(date_string, '%Y%m%d')
        date_ordinal = date.toordinal()
        # Get the value of the measurement, which in this case will be the temperature, and convert it to an integer.
        # Note that at this point the temperatures are still whole numbers in tenths of degrees.
        temp_string = fields[3]
        temp = int(fields[3])

        # Output a key value pair of the date and the temperature to the reducer, separated by a tab character.
        print('%d\t%d' % (date_ordinal, temp))
