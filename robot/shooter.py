""" Shooter Functions """
# importing packages
import wpilib
from ctre import *
from wpilib.controller import PIDController
# main shooter class
from robot import Dashboard


class Shooter:
    def __init__(self):
        # assigning functions
        self.dashboard = Dashboard()

        # shooter motors and encoders
        self.topShooterEncoder = WPI_TalonSRX(5)
        self.topShooterMotor = WPI_VictorSPX(6)
        self.bottomShooterEncoder = WPI_TalonSRX(7)
        self.bottomShooterMotor = WPI_VictorSPX(8)

        # inverses shooter motors
        self.topShooterMotor.setInverted(True)

        # shooter motor groups
        self.topMotors = wpilib.SpeedControllerGroup(self.topShooterEncoder, self.topShooterMotor)
        self.bottomMotors = wpilib.SpeedControllerGroup(self.bottomShooterEncoder, self.bottomShooterMotor)

        self.kP = 0.1
        self.kI = 0.01
        self.kD = 0.00

        # PID
        self.PIDShooterTop = PIDController(self.kP, self.kI, self.kD)
        self.PIDShooterTop.setTolerance(0)
        self.PIDShooterBottom = PIDController(self.kP, self.kI, self.kD)
        self.PIDShooterBottom.setTolerance(0)

        # storage for the ranges that the robot can shoot from
        # first number is the top rpm and second number is the bottom rpm
        self.rangesForShooting = [
            [50, 25],
            [40, 20],
            [30, 15]
        ]


    # def setPID(self, kP, kI, kD, motor):
    #     if motor == 'Top':
    #         self.PIDShooterTop.setPID(kP, kI, kD)
    #     if motor == 'Bottom':
    #         self.PIDShooterBottom.setPID(kP, kI, kD)
    #     if motor == 'Both':
    #         self.PIDShooterTop.setPID(kP, kI, kD)
    #         self.PIDShooterBottom.setPID(kP, kI, kD)

    def reset(self, motor):
        # resets shooter encoder and PID
        self.topShooterEncoder.setSelectedSensorPosition(0)
        self.bottomShooterEncoder.setSelectedSensorPosition(0)
        if motor == 'Top':
            self.PIDShooterTop.reset()
        if motor == 'Bottom':
            self.PIDShooterBottom.reset()
        if motor == 'Both':
            self.PIDShooterTop.reset()
            self.PIDShooterBottom.reset()


    def convertVelocityToRPM(velocity):
        """ This method will take in velocity and convert the velocity into rotations per minute

        :param velocity:
        :type velocity: float

        :return rpm:
        :rtype rpm: float
        """

        # convert velocity to rpm
        conversionFactor = 600 / 4096
        RPM = velocity * conversionFactor
        return RPM


    def getShooterRPM(self, motors):
        """ This method will get velocity return rpm of the top or bottom shooter speed controller group

        :return rpm:
        :rtype rpm: float
        """
        if motors == 'Top':
            topEncoderVelocity = self.topShooterEncoder.getSelectedSensorVelocity()
            topShooterRPM = Shooter.convertVelocityToRPM(topEncoderVelocity)
            return topShooterRPM

        elif motors == 'Bottom':
            bottomEncoderVelocity = self.bottomShooterEncoder.getSelectedSensorVelocity()
            bottomShooterRPM = Shooter.convertVelocityToRPM(bottomEncoderVelocity)
            return bottomShooterRPM
        
        elif motors == 'Both':
            topEncoderVelocity = self.topShooterEncoder.getSelectedSensorVelocity()
            topShooterRPM = Shooter.convertVelocityToRPM(topEncoderVelocity)
            bottomEncoderVelocity = self.bottomShooterEncoder.getSelectedSensorVelocity()
            bottomShooterRPM = Shooter.convertVelocityToRPM(bottomEncoderVelocity)
            shooterRPM = (topShooterRPM + bottomShooterRPM) / 2
            return shooterRPM


    def setShooterRPM(self, motors, setpoint):
        # conversion factor to account for incorrect RPM
        conversionFactor = 3.25
        setpoint = setpoint * conversionFactor
        if motors == 'Top':
            self.topMotors.set(self.PIDShooterTop.calculate(self.getShooterRPM('Top'), setpoint) / 1000)

        elif motors == 'Bottom':
            self.bottomMotors.set(self.PIDShooterBottom.calculate(self.getShooterRPM('Bottom'), setpoint) / 1950)

        elif motors == 'Both':
            self.topMotors.set(self.PIDShooterTop.calculate(self.getShooterRPM('Top'), setpoint) / 1000)
            # self.bottomMotors.set((self.PIDShooterBottom.calculate(self.getShooterRPM('Bottom'), setpoint)) / 1000)
            self.bottomMotors.set(self.PIDShooterBottom.calculate(self.getShooterRPM('Bottom'), setpoint) / 1950)

        elif motors == 'Stop':
            self.topMotors.stopMotor()
            self.bottomMotors.stopMotor()


    def shooterPower(self, topPower, bottomPower):
        self.topMotors.set(topPower)
        self.bottomMotors.set(bottomPower)


    def shootPreDefinedLengths(self, listIndexNumber):
        """ This method will set the rpm of the motors
        The top rpm and bottom rpm will be set based on the stored ranges
        We will get these values from the ranges if the index of the ranges equals the inputed number

        :param listIndexNumber:
        :type listIndexNumber: int

        :return void:
        """

        # set the shooter rpms to the extracted values
        # self.setTopShooterRPM(self.rangesForShooting[listIndexNumber][1])
        # self.setBottomShooterRPM(self.rangesForShooting[listIndexNumber][2])
        pass


    def shootAutonomous(self, distance):
        # automatically shoot balls given distance
        pass
