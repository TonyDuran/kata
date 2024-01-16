try:
    from raw_input import input
except ImportError:
    pass

import os
import sys
from datetime import datetime

def timeConversion(s):
    time_date = datetime.strptime(s, "%I:%M:%S%p")
    return time_date.strftime("%H:%M:%S")


time = input()
print(timeConversion(time))