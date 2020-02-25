""""" lift functions """
# importing packages
import wpilib
from ctre import *


class Lift:
    def __init__(self):
        # lift motor
        self.liftMotor = WPI_VictorSPX(13)

    def changeLift(self, liftButtonStatus):
        # changes the position of the lift
        pass

    def runMotor(self, runLiftButtonStatus):
        # runs motor if the 'y' button is being pressed
        if runLiftButtonStatus is True:
            self.liftMotor.set(1)
        elif runLiftButtonStatus is False:
            self.liftMotor.stopMotor()
