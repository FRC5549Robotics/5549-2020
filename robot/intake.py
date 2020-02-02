''' All Functions relating to Intake'''
# Importing Packages
import wpilib

class Intake:
    def __init__(self):
    # Motor for Intake
    intakeMotor = WPI_VictorSPX(9)
    scaling = 0.5

    def takeIn():
        # Function to Take In Ball
        intakeMotor.set(scaling)

    def eject():
        # Function to Eject Balls
        intakeMotor.set(-scaling)
