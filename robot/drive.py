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
        # PID
        self.PIDDrive = PIDController(0.1, 0.0, 0.0)
        self.PIDDrive.setTolerance(100)


    def setPID(self, kP, kI, kD):
        self.PIDDrive.setPID(kP, kI, kD)


    def getGearSolenoid(self):
        return self.gearSolenoid.get()


    def turnToAngle(self, angleNavx, angleLimelight):
        # turn robot to specified angle values using navx
        pass


    def turnToTarget(self, angleLimelight):
        # turn robot to limelight target
        error = 4
        if abs(angleLimelight) < error:
            pass
        elif angleLimelight < -error:
            self.drive.tankDrive(-0.75, -0.75)
        elif angleLimelight > error:
            self.drive.tankDrive(0.75, 0.75)
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