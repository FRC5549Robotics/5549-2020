""" Drive Functions """
# importing packages
import wpilib
import navx
from ctre import *
from wpilib.drive import DifferentialDrive
from wpilib.controller import PIDController


class Drive:
    def __init__(self):
        """ Drive Train """
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
        """ Resetting sensors """
        self.rearLeftEncoder.setSelectedSensorPosition(0)
        self.rearRightEncoder.setSelectedSensorPosition(0)
        self.navx.reset()

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint

    def setPID(self, kP, kI, kD):
        self.kP = kP
        self.kI = kI
        self.kP = kD

    def PID(self):      # does not work due to navx not working. see turnAngle() instead
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

    def execute(self):      # oes not work due to navx not working. see turnAngle() instead
        self.PID()
        if self.turnRight is True:
            self.drive.tankDrive(self.rcw, self.rcw)
        elif self.turnRight is False:
            self.drive.tankDrive(-self.rcw, -self.rcw)

    def getGearSolenoid(self):
        return self.gearSolenoid.get()

    def turnAngle(self, angle):
        """ Turn to specific angles for autonomous """
        # getting encoder position values and averaging
        leftEncoderValue = abs(self.rearLeftEncoder.getSelectedSensorPosition())
        rightEncoderValue = abs(self.rearRightEncoder.getSelectedSensorPosition())
        driveTrainEncoderValue = abs(rightEncoderValue + leftEncoderValue) / 2

        # converting encoder value to angles
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
        """ Turn robot to the limelight target """
        if angleLimelight > 15:
            nspeed = angleLimelight / 50
            self.drive.tankDrive(nspeed+0.1, nspeed+0.1)
        elif 5 < angleLimelight < 15:
            nspeed = angleLimelight / 75
            self.drive.tankDrive(nspeed+0.3, nspeed+0.3)
        elif 0 < angleLimelight < 5:
            self.drive.tankDrive(0.4, 0.4)
        elif -2 < angleLimelight < 2:
            self.drive.stopMotor()
        elif -5 < angleLimelight < 0:
            self.drive.tankDrive(-0.4, -0.4)
        elif -15 < angleLimelight < -5:
            nspeed = angleLimelight / 75
            self.drive.tankDrive(nspeed-0.3, nspeed-0.3)
        elif angleLimelight < -15:
            nspeed = angleLimelight / 50
            self.drive.tankDrive(nspeed-0.1, nspeed-0.1)

    def changeGear(self, buttonStatus):
        """ Switch gear between high and low """
        if buttonStatus is True:
            # high gear
            self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        elif buttonStatus is False:
            # low gear
            self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)

    def tankDrive(self, leftJoystickAxis, rightJoystickAxis):
        """ Tank drive at set scaling using both joysticks """
        scaling = 1
        self.drive.tankDrive(-leftJoystickAxis * scaling, rightJoystickAxis * scaling, True)

    def arcadeDrive(self, rightJoystickAxis, rotateAxis):
        """ Arcade drive at set scaling using the right joystick """
        scaling = 1
        self.drive.arcadeDrive(rotateAxis, -rightJoystickAxis * scaling, True)