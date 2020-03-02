""" vision functions """
# importing packages
import wpilib
from networktables import NetworkTables
import math


class Vision:
    def __init__(self):
        self.heightCamera = 20.0
        self.heightTarget = 115.25
        self.angleMount = 15  # change later

    def getDistance(self, ty):
        # finds distance to target using limelight
        if ty == None:
            pass
        else:
            distanceToTarget = ((self.heightTarget - self.heightCamera) / math.tan(self.angleMount + ty))
            return distanceToTarget