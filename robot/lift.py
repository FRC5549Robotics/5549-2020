""" Lift Functions """
import wpilib
from ctre import *


class Lift:
    def __init__(self):
        """ Lift """
        # lift motor
        self.liftMotor = WPI_VictorSPX(13)

        # lift pneumatics
        self.liftSolenoid = wpilib.DoubleSolenoid(4, 5)

        self.liftMotor.setInverted(True)


    def changeLift(self, liftButtonStatus):
        """ Changes the position of the lift """
        if liftButtonStatus is True:
            # lift up
            self.liftSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        elif liftButtonStatus is False:
            # lift down
            self.liftSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)


    def runMotor(self, runLift):
        """ Runs lift motor """
        if runLift > 0.5:
            self.liftMotor.set(1)
        else:
            self.liftMotor.stopMotor()
