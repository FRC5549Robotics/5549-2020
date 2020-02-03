''' All Functions relating to Drive'''
# Importing Packages
import wpilib

class Drive:
    def __init__(self):
        # Motors for Drive Train
        self.leftMotor1 = WPI_TalonSRX(1)
        self.leftMotor2 = WPI_TalonSRX(2)
        self.rightMotor1 = WPI_TalonSRX(3)
        self.rightMotor2 = WPI_TalonSRX(4)

        # Set Controller Grous
        self.leftDrive = wpilib.SpeedControllerGroup(leftMotor1, rightMotor2)
        self.rightDrive = wpilib.SpeedControllerGroup(rightMotor1, rightMotor2)

        # Drive Train
        self.drive = wpilib.DifferentialDrive(leftDrive, rightDrive)

        # Solenoid for Gear Shifting
        self.gearSolenoid = wpilib.DoubleSolenoid(0, 1)

    def turnToAngle(angle):
        # Turn Robot to Specified Decimal Values

    def changeGear(buttonStatus):
        # Switches Gear Mode
        if buttonStatus == True:
            # High Gear
            self.gearSolenoid.set(wpilib.gearSolenoid.Value.kForward)
        elif buttonStatus == False:
            # Low Gear
            self.gearSolenoid.set(wpilib.gearSolenoid.Value.kReverse)


    def tankDrive(leftJoystick, rightJoystick):
        # Tank Drive at Set Scaling
        scaling = 0.65
        drive.tankDrive(leftJoystick * scaling, rightJoystick * scaling)

    def arcadeDrive(leftJoystick, rotate):
        # Arcade Drive at Set Scaling
        scaling = 0.65
        drive.arcadeDrive(leftJoystick * scaling, rotate * scaling)
