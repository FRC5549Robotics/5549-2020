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
        self.frontRightMotor.setInverted(True)
        self.rearRightEncoder.setInverted(True)

        # drive train motor groups
        self.leftDrive = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftEncoder)
        self.rightDrive = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightEncoder)

        # setting up differential drive
        self.drive = DifferentialDrive(self.leftDrive, self.rightDrive)

        """ Pneumatics """
        # drive pneumatics
        self.gearSolenoid = wpilib.DoubleSolenoid(2, 3)    # check these numbers

        """ NavX """
        self.navx = navx.AHRS.create_spi()
        self.navx.reset()

        """ PID """
        # # pid constants
        # kP = 0.00
        # kI = 0.00
        # kD = 0.00
        # kF = 0.00

        # # pid controller
        # self.PIDNavX = PIDController(kP, kI, kD)
        # self.PIDNavX.setInputRange(0, 180)   # navx input - this says navx can go from 0 to 180 degrees
        #                                     # adjust as needed
        # self.PIDNavX.setOutputRange(-0.5, 0.5)  # adjusting power for now. check values and type
        # self.PIDNavX.setAbsoluteTolerance(1.0)  # setting the max it can miss by - 1 degrees
        # self.PIDNavX.setContinuous(True)    # check to see if we need this

    # def pidWrite(self, output):
    #     self.turnRate = output

    def getGearSolenoid(self):
        return self.gearSolenoid.get()

    def turnToAngle(self, turnButtonStatus, angle):
        # turn robot to specified angle values using navx
        if turnButtonStatus is True:
            if self.navx.getAngle():
                self.drive.tankDrive(0.5, -0.5)
        else:
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
        scaling = 1
        self.drive.tankDrive(-leftJoystickAxis * scaling, rightJoystickAxis * scaling, True)

    def arcadeDrive(self, rightJoystickAxis, rotateAxis):
        # arcade drive at set scaling
        scaling = 1
        self.drive.arcadeDrive(rotateAxis, -rightJoystickAxis * scaling, True)

