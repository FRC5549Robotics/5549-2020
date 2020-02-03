''' All Functions relating to Shooter'''
# Importing Packages
import wpilib

class Shooter:
    def __init__(self):
        # Encoders
        self.topShooter1Encoder = WPI_TalonSRX(4)
        self.topShooter2 = WPI_TalonSRX(5)
        self.bottomShooter1Encoder = WPI_TalonSRX(6)
        self.bottomShooter2 = WPI_TalonSRX(7)

        # Set Top and Bottom Shooters
        self.topShooters = wpilib.SpeedControllerGroup(topShooter1Encoder, topShooter2)
        self.bottomShooter = wpilib.SpeedControllerGroup(bottomShooter1Encoder, bottomShooter2)

        # Setting Shooter RPM
        # Need to Move to Always Check
        self.topShooterRPM = topShooter1Encoder.getQuadraturePosition()
        self.bottomShooterRPM = bottomShooter1Encoder.getQuadraturePosition()

    def shootFar(self):
        # Shoot the Ball for Set Far Distance
        self.initializeShooter(highrpm)

    def shootMid(self):
        # Shoot the Ball for Set Medium Distance
        self.initializeShooter(midrpm)

    def shootShort(self):
        # Shoot the Ball for Set Short Distance
        self.initializeShooter(lowrpm)

    def shootAuto(self, distance):
        # Automatically Shoot Balls Given Distance

    def initializeShooter(self, rpm):
        # Initializes Shooter and Moves Piston
        # Only for Shooter Functions
        self.topShooters.set(rpm)
        self.bottomShooters.set(rpm)
