""" Vision Functions """
import wpilib
from networktables import NetworkTables
import math


class Vision:
    def __init__(self):
        """ Vision """
        # set variables
        self.heightCamera = 20.0
        self.heightTarget = 98.25
        self.angleMount = 24.25  # change later

    def getDistance(self, ty):
        """ Calculates distance using limelight """
        if ty == None:
            # passes if there is no target
            pass
        else:
            # calculates distance to the target if an angle is found
            self.angle = (self.angleMount + ty) * math.pi / 180
            distanceToTarget = ((self.heightTarget - self.heightCamera) / math.tan(self.angle))
            return distanceToTarget