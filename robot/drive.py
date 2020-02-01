''' All Functions relating to Drive'''
# Importing Packages
import wpilib

class Drive:
    def __init__(self):
        # Motors for Drive Train
        leftMotor1 = WPI_TalonSRX(1)
        leftMotor2 = WPI_TalonSRX(2)
        rightMotor1 = WPI_TalonSRX(3)
        rightMotor2 = WPI_TalonSRX(4)

        # Set Controller Grous
        leftDrive = wpilib.SpeedControllerGroup(leftMotor1, rightMotor2)
        rightDrive = wpilib.SpeedControllerGroup(rightMotor1, rightMotor2)

        # Drive Train
        drive = wpilib.drive.DifferentialDrive(left, right)

        # Solenoid for Gear Shifting
        self.DoubleSolenoidOne = wpilib.DoubleSolenoid(0, 1)

    def turnToAngle(angle):
        # Turn Robot to Specified Decimal Values

    def changeGear(buttonStatus):
        # Switches Gear Mode
        if buttonStatus == True:
            # High Gear
            self.DoubleSolenoidOne.set(wpilib.DoubleSolenoid.Value.kForward)
        elif buttonStatus == False:
            # Low Gear
            self.DoubleSolenoidOne.set(wpilib.DoubleSolenoid.Value.kReverse)


    def tankDrive(leftJoystick, rightJoystick):
        # Tank Drive at Set Scaling
        scaling = 0.65
        drive.tankDrive(leftJoystick * scaling, rightJoystick * scaling)

    def arcadeDrive(leftJoystick, rotate):
        # Arcade Drive at Set Scaling
        scaling = 0.65
        drive.arcadeDrive(leftJoystick * scaling, rotate * scaling)
