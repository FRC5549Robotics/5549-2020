""" shooter functions """
# importing packages
import wpilib
from ctre import *

class Shooter:
    def __init__(self):
        # shooter motors and encoders
        self.topShooter1Encoder = WPI_TalonSRX(1)
        self.topShooter2 = WPI_Talon(2)
        self.bottomShooter1Encoder = WPI_TalonSRX(3)
        self.bottomShooter2 = WPI_Talon(4)

        # shooter motor groups
        self.topMotors = wpilib.SpeedControllerGroup(self.topShooter1Encoder, self.topShooter2)
        self.bottomMotors = wpilib.SpeedControllerGroup(self.bottomShooter1Encoder, self.bottomShooter2)

        # setting shooter rpm
        # need to move to always check
        self.topShooterRPM = self.topShooter1Encoder.getQuadraturePosition()    # this is not actually rpm
        self.bottomShooterRPM = self.bottomShooter1Encoder.getQuadraturePosition()  # this is not actually rpm

    def shootFar(self):
        # shoot the ball for set far distance
        self.highrpm = 0 # add later
        self.initializeShooter(self.highrpm)

    def shootMid(self):
        # shoot the ball for set medium distance
        self.midrpm = 0 # add later
        self.initializeShooter(self.midrpm)

    def shootShort(self):
        # shoot the ball for set short distance
        self.lowrpm = 0 # add later
        self.initializeShooter(self.lowrpm)

    def shootAuto(self, distance):
        # automatically shoot balls given distance
        pass

    def initializeShooter(self, rpm):
        # initializes shooter and moves piston
        # only for shooter functions
        self.topMotors.set(rpm)
        self.bottomMotors.set(rpm)