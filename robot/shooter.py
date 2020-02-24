""" shooter functions """
# importing packages
import wpilib
from ctre import *


# main shooter class
class Shooter:
    def __init__(self):
        # shooter motors and encoders
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

        # storage for the ranges that the robot can shoot from
        # first number is the top rpm
        # second number is the bottom rpm
        self.rangesForShooting = [
            [50, 25],
            [40, 20],
            [30, 15]
        ]

    def getTopShooterRpm(self):
        """ This method will return rpm of the top shooter speed controller group

        :return rpm:
        :rtype rpm: float
        """

        rawTopEncoderVelocity = self.topShooter1Encoder.getSelectedSensorVelocity()  # get velocity
        rpm = Shooter.convertVelocityToRpm(rawTopEncoderVelocity)  # convert to rpm
        return rpm

    def getBottomShooterRpm(self):
        """ This method will return the rpm of the bottom shooter speed controller group

        :return rpm:
        :rtype rpm: float
        """

        rawBottomEncoderVelocity = self.bottomShooter1Encoder.getSelectedSensorVelocity()  # get velocity
        rpm = Shooter.convertVelocityToRpm(rawBottomEncoderVelocity)  # convert to rpm
        return rpm

    def setTopShooterRpm(self, rpm):
        self.topMotors.set(rpm)

    def setBottomShooterRpm(self, rpm):
        self.bottomMotors.set(rpm)

    # call this function with the name of the range in words
    # for example, you can call shootPreDefinedLengths('far')
    def shootPreDefinedLengths(self, listIndexNumber):
        """ This method will set the rpm of the motors
        The top rpm and bottom rpm will be set based on the stored ranges
        We will get these values from the ranges if the index of the ranges equals the inputed number

        :param listIndexNumber:
        :type listIndexNumber: int

        :return void:
        """

        # set the shooter rpms to the extracted values
        self.setTopShooterRpm(self.rangesForShooting[listIndexNumber][1])
        self.setBottomShooterRpm(self.rangesForShooting[listIndexNumber][2])

    def shootAutonomous(self, distance):
        # automatically shoot balls given distance
        pass

    def initializeShooter(self, shoot):
        # automatically shoot balls given distance
        pass

    def PIDShooter(self):
        kP = 0.00
        kI = 0.00
        kD = 0.00
        kf = 0.00
        self.PIDShooter = wpilib.PIDController(self, kp, kI, kD, kF, self.encoder, output=self)

    @staticmethod
    def convertVelocityToRpm(rawVelocity):
        """ This method will take in velocity and convert the velocity into rotations per minute

        :param rawVelocity:
        :type rawVelocity: float

        :return rpm:
        :rtype rpm: float
        """

        # convert velocity to rpm
        conversionFactor = 600 / 4096
        rpm = rawVelocity * conversionFactor
        return rpm