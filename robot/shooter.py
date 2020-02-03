""" shooter functions """
# importing packages
import wpilib
from ctre import *

class Shooter:
    def __init__(self):
        # shooter motors and encoders
        self.topShooter1Encoder = WPI_TalonSRX(4)
        self.topShooter2 = WPI_TalonSRX(5)
        self.bottomShooter1Encoder = WPI_TalonSRX(6)
        self.bottomShooter2 = WPI_TalonSRX(7)

        # shooter motor groups
        self.topMotors = wpilib.SpeedControllerGroup(self.topShooter1Encoder, self.topShooter2)
        self.bottomMotors = wpilib.SpeedControllerGroup(self.bottomShooter1Encoder, self.bottomShooter2)

        # setting shooter rpm
        # need to move to always check
        self.topShooterRPM = self.topShooter1Encoder.getQuadraturePosition()    # this is not actually rpm
        self.bottomShooterRPM = self.bottomShooter1Encoder.getQuadraturePosition()  # this is not actually rpm

    def shootFar(self, highrpm):
        # shoot the ball for set far distance
        self.initializeShooter(highrpm)

    def shootMid(self, midrpm):
        # shoot the ball for set medium distance
        self.initializeShooter(midrpm)

    def shootShort(self, lowrpm):
        # shoot the ball for set short distance
        self.initializeShooter(lowrpm)

    def shootAuto(self, distance):
        # automatically shoot balls given distance
        pass

    def initializeShooter(self, rpm):
        # initializes shooter and moves piston
        # only for shooter functions
        self.topMotors.set(rpm)
        self.bottomMotors.set(rpm)
