from collections import namedtuple

Coordinates = namedtuple('Coordinates', ["lat", "lon"])

ivy_tech = Coordinates(41.112926, -85.112030)
print(ivy_tech)
print(type(ivy_tech))