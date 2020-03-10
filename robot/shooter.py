""" Shooter Functions """
import wpilib
from ctre import *
from wpilib.controller import PIDController


class Shooter:
    def __init__(self):
        """ Shooter """
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

        """ Shooter PID """
        # top PID
        self.kPTop = 0.25  # 0.9    # 0.1
        self.kITop = 0.07  # 0.009  # 0.001
        self.kDTop = 0.02  # 0      # 0
        self.kFTop = 1.0  # 1.035  # 1.15

        self.integralTop = 0
        self.previousErrorTop = 0
        self.setpointTop = 0

        # bottom PID
        self.kPBottom = 0.1   # 0.9   # 0.105
        self.kIBottom = 0.02   # 0.009 # 0.001
        self.kDBottom = 0.02   # 0     # 0
        self.kFBottom = 1.0   # 0.932 # 0.999

        self.integralBottom = 0
        self.previousErrorBottom = 0
        self.setpointBottom = 0
        

    def convertVelocityToRPM(velocity):
        """ This method will take in velocity and convert the velocity into rotations per minute

        :param rawVelocity:
        :type rawVelocity: float
        :return rpm:
        :rtype rpm: float
        """
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


    def setSetpoint(self, PID, setpoint):
        """ Sets the setpoints of the top or bottom shooter motors """
        if PID == 'Top':
            self.setpointTop = setpoint
        elif PID == 'Bottom':
            self.setpointBottom = setpoint


    def setVarPID(self, kP, kI, kD, kF, motor):
        """ Sets the variables for PID to be set """
        if motor == 'Top':
            self.kPTop = kP
            self.kITop = kI
            self.kDTop = kD
            self.kFTop = kF
        if motor == 'Bottom':
            self.kPBottom = kP
            self.kIBottom = kI
            self.kDBottom = kD
            self.kFBottom = kF


    def setPID(self, PID):
        """ Method to set two different PIDs for top shooter and bottom shooter with a backspin on bottom shooter """
        if PID == 'Top':
            errorTop = self.setpointTop - self.getShooterRPM('Top')
            self.integralTop = self.integralTop + errorTop

            if self.integralTop > 4400:
                self.integralTop = 4400

            derivative = errorTop - self.previousErrorTop
            self.rcwTop = (self.kPTop * errorTop) + (self.kITop * self.integralTop) + (self.kDTop * derivative) + (self.kFTop * self.setpointTop)
            self.PIDTopOutput = self.rcwTop / 4400
            self.previousErrorTop = errorTop

        elif PID == 'Bottom':
            errorBottom = abs(self.setpointBottom) - abs(self.getShooterRPM('Bottom'))
            self.integralBottom = self.integralBottom + errorBottom

            if self.integralBottom > 4400:
                self.integralBottom = 4400

            derivative = errorBottom - self.previousErrorBottom
            self.rcwBottom = (self.kPBottom * errorBottom) + (self.kIBottom * self.integralBottom) + (self.kDBottom * derivative) + (self.kFBottom * self.setpointBottom)
            self.PIDBottomOutput = self.rcwBottom / 4400
            self.previousErrorBottom = errorBottom

    def execute(self, PID):
        """ Executes the drive-train PID """
        if PID == 'Top':
            self.setPID('Top')
            self.topMotors.set(self.PIDTopOutput)
        elif PID == 'Bottom':
            self.setPID('Bottom')
            self.bottomMotors.set(self.PIDBottomOutput)