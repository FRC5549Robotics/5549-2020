""" vision functions """
# importing packages
import wpilib
from robot.shared import *
from networktables import NetworkTables
import math


class Vision:

    def __init__(self):
        self.limelight = NetworkTables.getTable("limelight")

    def alignTarget(self) -> float:
        horizontalTargetAngle = self.limelight.getNumber('tx', -1)

        return math.radians(horizontalTargetAngle)*ROBOTRADIUS*0.95 #0.95 is a coefficient to prevent overshoot.

    def getDistance(self) -> float:
        verticalTargetAngle = self.limelight.getNumber('ty', -1)  # finds vertical angle to target
        if verticalTargetAngle is -1: return -1

        # finds distance to target using limelight
        return (TARGETHEIGHT - CAMHEIGHTMOUNT) / math.tan(math.radians(CAMANGLEMOUNT + verticalTargetAngle)) + CAMOFFSETMOUNT