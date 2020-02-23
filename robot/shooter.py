""" shooter functions """
# importing packages
import wpilib
from ctre import *


class Shooter:
    def __init__(self):
        # shooter motors
        self.topShooterEncoder = WPI_TalonSRX(5)
        self.topShooterMotor = WPI_VictorSPX(6)
        self.bottomShooterEncoder = WPI_TalonSRX(7)
        self.bottomShooterMotor = WPI_VictorSPX(8)

        # inverses shooter motors
        self.topShooterEncoder.setInverted(True)
        self.bottomShooterEncoder.setInverted(True)

        # shooter motor groups
        self.topMotors = wpilib.SpeedControllerGroup(self.topShooterEncoder, self.topShooterMotor)
        self.bottomMotors = wpilib.SpeedControllerGroup(self.bottomShooterEncoder, self.bottomShooterMotor)

        # setting shooter rpm
        # need to move to always check
        self.topShooterRPM = self.topShooterEncoder.getSelectedSensorVelocity()    # this is not actually rpm
        self.bottomShooterRPM = self.topShooterMotor.getSelectedSensorVelocity()  # this is not actually rpm

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
        self.lowrpm = 0     # add later
        self.initializeShooter(self.lowrpm)

    def shootAuto(self, distance):
        # automatically shoot balls given distance
        pass

    def initializeShooter(self, rpm):
        # initializes shooter and moves piston
        # only for shooter functions
        self.topMotors.set(rpm)
        self.bottomMotors.set(rpm)