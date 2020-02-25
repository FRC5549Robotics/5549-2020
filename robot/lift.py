""""" lift functions """
# importing packages
import wpilib
from ctre import *


class Lift:
    def __init__(self):
        # lift motor
        self.liftMotor = WPI_VictorSPX(13)

        # lift pneumatics
        self.liftSolenoid = wpilib.DoubleSolenoid(4, 5)

    def changeLift(self, liftButtonStatus):
        # changes the position of the lift
        if liftButtonStatus is True:
            # lift out - test to see if kForward is actually lift out in this case
            self.liftSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        elif liftButtonStatus is False:
            # lift in - test to see if kReverse if actually lift in in this case
            self.liftSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)

    def runMotor(self, runLiftButtonStatus):
        # runs motor if the 'y' button is being pressed
        if runLiftButtonStatus is True:
            self.liftMotor.set(1)
        elif runLiftButtonStatus is False:
            self.liftMotor.stopMotor()
