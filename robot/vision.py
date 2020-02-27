""" vision functions """
# importing packages
import wpilib
from networktables import NetworkTables
import math


class Vision:
    def __init__(self):
        self.heightCamera = 0  # change later
        self.heightTarget = 0  # change later
        self.angleMount = 0  # change later

    # def getDistance(self, ty):
    #     # finds distance to target using limelight
    #     self.distanceToTarget = (self.heightTarget - self.heightCamera) / math.tan(self.angleMount + self.verticalAngleToTarget)