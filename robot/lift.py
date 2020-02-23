""""" lift functions """
# importing packages
import wpilib
from ctre import *


class Lift:
    def __init__(self):
        # lift motor
        self.liftMotor = WPI_VictorSPX(10)

    def changeLift(self, liftButtonStatus):
        # changes the position of the lift
        pass

    def runMotor(self, power):
        # runs motor at set power
        self.liftMotor.set(power)
