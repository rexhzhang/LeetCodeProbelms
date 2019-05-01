from enum import Enum
class Vehicle (Enum):
    motorcycle = 1
    car = 2
    truck = 3
    bus = 4

motorCycle = Vehicle.motorcycle
print(motorCycle)