""" vision functions """
# importing packages
import wpilib
from networktables import NetworkTables
import math


class Vision:
    def __init__(self):
        self.heightCamera = 20.0
        self.heightTarget = 98.25
        self.angleMount = 24.25  # change later

    def getDistance(self, ty):
        # finds distance to target using limelight
        if ty == None:
            pass
        else:
            self.angle = (self.angleMount + ty) * math.pi / 180
            distanceToTarget = ((self.heightTarget - self.heightCamera) / math.tan(self.angle))
            return distanceToTarget