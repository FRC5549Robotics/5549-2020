''' All Functions relating to Intake'''
# Importing Packages
import wpilib

class Intake:
    def __init__(self):
    # Motor for Intake
    self.intakeMotor = WPI_VictorSPX(9)
    scaling = 0.5

    def takeIn():
        # Function to Take In Ball
        self.intakeMotor.set(scaling)

    def eject():
        # Function to Eject Balls
        self.intakeMotor.set(-scaling)
