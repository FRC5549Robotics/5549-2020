""" drive functions """
# importing packages
import wpilib
from ctre import *
from wpilib.drive import DifferentialDrive

class Drive:
    def __init__(self):
        # drive train motors
        self.leftMotor1 = WPI_TalonSRX(1)
        self.leftMotor2 = WPI_TalonSRX(2)
        self.rightMotor1 = WPI_TalonSRX(3)
        self.rightMotor2 = WPI_TalonSRX(4)

        # drive train motor groups
        self.leftDrive = wpilib.SpeedControllerGroup(self.leftMotor1, self.rightMotor2)
        self.rightDrive = wpilib.SpeedControllerGroup(self.rightMotor1, self.rightMotor2)

        # setting up differential drive
        self.drive = DifferentialDrive(self.leftDrive, self.rightDrive)

        # pneumatic solenoid for gear shifting
        self.gearSolenoid = wpilib.DoubleSolenoid(0, 1)

    def turnToAngle(self, angle):
        # turn robot to specified angle values using navx
        pass

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
        scaling = 0.65
        self.drive.tankDrive(leftJoystickAxis * scaling, rightJoystickAxis * scaling)

    def arcadeDrive(self, leftJoystick, rotateAxis):
        # arcade drive at set scaling
        scaling = 0.65
        self.drive.arcadeDrive(leftJoystick * scaling, rotateAxis * scaling)
