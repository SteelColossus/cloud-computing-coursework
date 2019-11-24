#!/usr/bin/env python
"""mapper.py"""

import sys
from datetime import datetime

station_id_to_capture = 'UK000003377' # Either UK000056225 (Oxford) or UK000003377 (Waddington)

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    station_id = fields[0]
    measure = fields[2]
    quality = fields[5]

    if station_id == station_id_to_capture and (measure == 'TMAX' or measure == 'TMIN') and quality == '':
        date_string = fields[1]
        date = datetime.strptime(date_string, '%Y%m%d')
        date_ordinal = date.toordinal()
        temp_string = fields[3]
        temp = int(fields[3])

        print('%d\t%d' % (date_ordinal, temp))
