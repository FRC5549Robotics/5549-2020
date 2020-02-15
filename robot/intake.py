""" intake functions """
# importing packages
import wpilib
from ctre import *

class Intake:
    def __init__(self):
        # intake motor
        self.intakeMotor = WPI_VictorSRX(6)

    def takeIn(self):
        # taking in the ball at set scaling
        scaling = 0.50
        self.intakeMotor.set(scaling)

    def eject(self):
        # ejecting ball at set scaling
        scaling = 0.50
        self.intakeMotor.set(-scaling)
