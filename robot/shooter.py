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
        # self.topShooterEncoder.setInverted(True)
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

    def getShooterRpm(self, motors):
        """ This method will get velocity return rpm of the top or bottom shooter speed controller group

        :return rpm:
        :rtype rpm: float
        """
        if motors == 'Top':
            topEncoderVelocity = self.topShooter1Encoder.getSelectedSensorVelocity()
            topRPM = Shooter.convertVelocityToRpm(topEncoderVelocity)
            return topRPM
        elif motors == 'Bottom':
            bottomEncoderVelocity = self.bottomShooter2Encoder.getSelectedSensorVelocity() 
            bottomRPM = Shooter.convertVelocityToRpm(BottomEncoderVelocity)
            return bottomRPM
        
    def setShooterRpm(self, motors, rpm):
        if motors == 'Top':
            self.topMotors.set(rpm)
        elif motors == 'Bottom':
            self.bottomMotors.set(rpm)
        elif motors == 'Both':
            self.topMotors.set(rpm)
            self.bottomMotors.set(rpm)
        else:
            self.topMotors.stopMotor()
            self.bottomMotors.stopMotor()

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
        # start up shooter motors before shooting
        pass

    def PIDShooter(self):
        kP = 0.00
        kI = 0.00
        kD = 0.00
        kf = 0.00
        self.PIDShooter = wpilib.PIDController(self, kp, kI, kD, kF, self.encoder, output=self)

    @staticmethod
    def convertVelocityToRpm(velocity):
        """ This method will take in velocity and convert the velocity into rotations per minute

        :param velocity:
        :type velocity: float

        :return rpm:
        :rtype rpm: float
        """

        # convert velocity to rpm
        conversionFactor = 600 / 4096
        rpm = velocity * conversionFactor
        return rpm