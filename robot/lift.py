""""" lift functions """
# importing packages
import wpilib
from ctre import *

class Lift:
    def __init__(self):
        # lift motor
        self.liftMotor = WPI_VictorSPX(10)

    def dropDown(self):
        # drops the lift to down position
        pass

    def liftUp(self):
        # moves the lift to up position
        pass

    def runMotor(self, power):
        # runs motor at set power
        self.liftMotor.set(power)
