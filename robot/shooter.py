''' All Functions relating to Shooter'''
# Importing Packages
import wpilib

class Shooter:
    def __init__(self):
        # Encoders
        self.topShooter1Encoder = WPI_TalonSRX(4)
        topShooter2 = WPI_TalonSRX(5)
        self.bottomShooter1Encoder = WPI_TalonSRX(6)
        bottomShooter2 = WPI_TalonSRX(7)

        # Set Top and Bottom Shooters
        topShooters = wpilib.SpeedControllerGroup(topShooter1Encoder, topShooter2)
        bottomShooter = wpilib.SpeedControllerGroup(bottomShooter1Encoder, bottomShooter2)

        # Setting Shooter RPM
        topShooterRPM = topShooter1Encoder.getQuadraturePosition()
        bottomShooterRPM = bottomShooter1Encoder.getQuadraturePosition()

    def shootFar(self):
        # Shoot the Ball for Set Far Distance

    def shootMid(self):
        # Shoot the Ball for Set Medium Distance

    def shootShort(self):
        # Shoot the Ball for Set Short Distance

    def shootAuto(self, distance):
        # Automatically Shoot Balls Given Distance

    def initializeShooter(self):
        # Initializes Shooter and Moves Piston
        # Only for Shooter Functions
