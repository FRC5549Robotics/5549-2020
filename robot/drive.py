""" Drive Functions """
# importing packages
import wpilib
import navx
from ctre import *
from wpilib.drive import DifferentialDrive
from wpilib.controller import PIDController


class Drive:
    def __init__(self):
        """ Drive """
        # drive train motors
        self.frontLeftMotor = WPI_VictorSPX(1)
        self.frontRightMotor = WPI_VictorSPX(2)
        self.rearRightEncoder = WPI_TalonSRX(3)
        self.rearLeftEncoder = WPI_TalonSRX(4)

        # reverses direction of drive train motors
        self.rearRightEncoder.setInverted(True)
        self.frontRightMotor.setInverted(True)

        # drive train motor groups
        self.leftDrive = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftEncoder)
        self.rightDrive = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightEncoder)

        # setting up differential drive
        self.drive = DifferentialDrive(self.leftDrive, self.rightDrive)


        """ Pneumatics """
        # drive pneumatics
        self.gearSolenoid = wpilib.DoubleSolenoid(2, 3)


        """ NavX """
        self.navx = navx.AHRS.create_spi()
        self.navx.reset()

        """ PID """
        self.setpoint = 0
        self.kP = 0.1
        self.kI = 0
        self.kD = 0

        self.integral = 0
        self.previousError = 0

        self.resetAngle = True


    def reset(self):
        self.rearLeftEncoder.setSelectedSensorPosition(0)
        self.rearRightEncoder.setSelectedSensorPosition(0)


    def setSetpoint(self, setpoint):
        self.setpoint = setpoint


    def setPID(self, kP, kI, kD):
        self.kP = kP
        self.kI = kI
        self.kP = kD


    def PID(self):
        if self.getGearSolenoid() == 2:
            self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        self.error = self.setpoint - (self.navx.getAngle() % 360)
        self.integral = self.integral + (self.error * .02)
        self.derivative = (self.error - self.previousError) / 0.02
        if abs(self.setpoint - (self.navx.getAngle() % 360)) > 180:
            self.turnRight = True
        elif abs(self.setpoint - (self.navx.getAngle() % 360)) < 180:
            self.turnRight = False
        self.rcw = (self.kP * self.error) + (self.kI * self.integral) + (self.kD * self.derivative)
        self.rcw = self.rcw * 0.5


    def execute(self):
        self.PID()
        if self.turnRight is True:
            self.drive.tankDrive(self.rcw, self.rcw)
        elif self.turnRight is False:
            self.drive.tankDrive(-self.rcw, -self.rcw)


    def getGearSolenoid(self):
        return self.gearSolenoid.get()


    def turnAngle(self, angle):
        # turn robot to specified angle values using navx
        leftEncoderValue = abs(self.rearLeftEncoder.getSelectedSensorPosition())
        rightEncoderValue = abs(self.rearRightEncoder.getSelectedSensorPosition())
        driveTrainEncoderValue = abs(rightEncoderValue + leftEncoderValue) / 2
        self.targetAngleEncoder = abs((4096 / 90) * angle)
        if angle > 0:
            self.targetAngleEncoder = self.targetAngleEncoder + 1024
        elif angle < 0:
            self.targetAngleEncoder = self.targetAngleEncoder + 256

        if driveTrainEncoderValue <= self.targetAngleEncoder:
            if angle > 0:
                self.drive.tankDrive(1, 1)
            if angle < 0:
                self.drive.tankDrive(-1, -1)
            self.resetAngle = False
        elif driveTrainEncoderValue >= (self.targetAngleEncoder + 1024):
            self.resetAngle = True
        else:
            self.leftDrive.stopMotor()
            self.rightDrive.stopMotor()

    def turnToTarget(self, angleLimelight):
        # turn robot to limelight target
        # error = 2
        # if angleLimelight < -error:
        #     self.drive.tankDrive(-0.75, -0.75)
        # elif angleLimelight > error:
        #     self.drive.tankDrive(0.75, 0.75)
        if abs(angleLimelight) >= 2:  # just proportional smoothing
            nspeed = angleLimelight / 35
            self.drive.tankDrive(nspeed+0.2, nspeed+0.2)
        return

    def changeGear(self, buttonStatus):
        # switches gear mode
        if buttonStatus is True:
            # high gear
            self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        elif buttonStatus is False:
            # low gear
            self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)


    def tankDrive(self, leftJoystickAxis, rightJoystickAxis):
        # tank drive at set scaling
        scaling = 1
        self.drive.tankDrive(-leftJoystickAxis * scaling, rightJoystickAxis * scaling, True)


    def arcadeDrive(self, rightJoystickAxis, rotateAxis):
        # arcade drive at set scaling
        scaling = 1
        self.drive.arcadeDrive(rotateAxis, -rightJoystickAxis * scaling, True)