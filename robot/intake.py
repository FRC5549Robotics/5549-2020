""" intake functions """
# importing packages
import wpilib
from ctre import *


class Intake:
    def __init__(self):
        # intake motor
        self.intakeMotor = WPI_TalonSRX(11)

        # reverse intake motor
        self.intakeMotor.setInverted(True)

    def takeIn(self):
        # taking in the ball at set scaling
        scaling = 0.50
        self.intakeMotor.set(scaling)

    def eject(self):
        # ejecting ball at set scaling
        scaling = 0.50
        self.intakeMotor.set(-scaling)
