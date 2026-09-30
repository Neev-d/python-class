import sensors

readings = [62, 84, 71]
print("threshold:", sensors.THRESHOLD)
print("average:", sensors.average(readings))
for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")

import sensors
print("__name__inside main.py is:", __name__)
print("__name__ inside sensors.py is:", sensors.__name__)

import sensors
from sensors import is_alert
import sensors as sn

print(sensors.is_alert(85))
print(is_alert(85))
print(sn.is_alert(85))

from sensors import *

THRESHOLD = 30.0
print("my THRESHOLD is", THRESHOLD)
print("is_alert950 says", is_alert(50))