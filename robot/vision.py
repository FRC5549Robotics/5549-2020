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

        # self.verticalAngleToTarget = NetworkTables.getTable("limelight").getNumber('ty', None) # finds vertical angle to target
        # self.horizontalAngleToTarget = NetworkTables.getTable("limelight").getNumber('tx', None) # finds horizontal angle to target

    # def getDistance(self):
    #     # finds distance to target using limelight
    #     self.distanceToTarget = (self.heightTarget - self.heightCamera) / math.tan(self.angleMount + self.verticalAngleToTarget)