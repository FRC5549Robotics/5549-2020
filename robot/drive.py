""" Drive Functions """
# importing packages
import wpilib
from ctre import *
from wpilib.drive import DifferentialDrive


class Drive:
    def __init__(self):
        # drive train motors
        self.frontLeftMotor = WPI_VictorSPX(1)
        self.frontRightMotor = WPI_VictorSPX(2)
        self.rearRightEncoder = WPI_TalonSRX(3)
        self.rearLeftEncoder = WPI_TalonSRX(4)

        # reverses direction of drive train motors
        self.frontRightMotor.setInverted(True)
        self.rearRightEncoder.setInverted(True)

        # drive train motor groups
        self.leftDrive = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftEncoder)
        self.rightDrive = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightEncoder)

        # setting up differential drive
        self.drive = DifferentialDrive(self.leftDrive, self.rightDrive)

        # drive pneumatics
        # self.gearSolenoid = wpilib.DoubleSolenoid(2, 3)    # check these numbers

    def getGearSolenoid(self):
        return self.gearSolenoid.get()

    def turnToAngle(self, angle):
        # turn robot to specified angle values using navx
        pass

    def changeGear(self, buttonStatus):
        # switches gear mode
        if buttonStatus is True:
            # high gear
            # self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
            pass
        elif buttonStatus is False:
            # low gear
            # self.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
            pass

    def tankDrive(self, leftJoystickAxis, rightJoystickAxis):
        # tank drive at set scaling
        scaling = 0.5
        self.drive.tankDrive(-leftJoystickAxis * scaling, rightJoystickAxis * scaling, True)

    def arcadeDrive(self, rightJoystickAxis, rotateAxis):
        # arcade drive at set scaling
        scaling = 0.5
        # self.drive.arcadeDrive(rightJoystickAxis * scaling, rotateAxis, True)
        self.drive.arcadeDrive(rotateAxis, -rightJoystickAxis * scaling, True)