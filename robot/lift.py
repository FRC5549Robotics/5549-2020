''' All Functions relating to Lift'''
# Importing Packages
import wpilib

class Lift:
    def __init__(self):
    self.liftMotor = WPI_VictorSPX(15)

    def dropDown():
        # Drops the Lift to Down Position

    def liftUp():
        # Moves the Lift to Up Position

    def runMotor(self, power):
        # Runs Motor at Set Power using Percent of Controller
        self.liftMotor.set(power)
