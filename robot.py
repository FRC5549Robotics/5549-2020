"""
Infinite Recharge - Manticore from FRC 5549: Gryphon Robotics
"""
# import packages
import wpilib
import navx
from ctre import *
from robot import *
from networktables import NetworkTables
from robotpy_ext.control.toggle import Toggle
from wpilib.drive import DifferentialDrive
import navx

"""
Motor Mapping
1 (Victor SPX - Positive): frontLeftMotor
2 (Victor SPX - Negative): frontRightMotor
3 (Talon SRX - Negative): rearRightEncoder
4 (Talon SRX - Positive): rearLeftEncoder
5 (Talon SRX - Negative): topShooterEncoder
6 (Victor SPX - Positive): topShooterMotor
7 (Talon SRX - Negative): bottomShooterEncoder
8 (Victor SPX - Positive): bottomShooterMotor
9 (Talon SRX - Positive): verticalIndexerRight
10 (Victor SPX - Positive): verticalIndexerLeft
11 (Talon SRX - Positive): intakeMotor
12 (Talon SRX - Negative): flatIndexer
13 (Victor SPX): liftMotor
14 (Talon SRX - Negative): semiCircleMotor
20 (Victor SPX): extraMotorController
"""


class Manticore(wpilib.TimedRobot):
    def robotInit(self):
        # adding functions
        self.dashboard = Dashboard()
        self.drive = Drive()
        self.indexer = Indexer()
        self.intake = Intake()
        self.lift = Lift()
        self.semicircle = Semicircle()
        self.shooter = Shooter()
        self.vision = Vision()

        """ Joystick """
        # setting joysticks and xbox controllers
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        self.xbox = wpilib.Joystick(2)

        """ Button Status and Toggles """
        # button for switching between arcade and tank drive
        self.driveButtonStatus = Toggle(self.rightJoystick, 2)

        # button for gear shifting
        self.gearButtonStatus = Toggle(self.rightJoystick, 1)

        # button for lift
        self.liftButtonStatus = Toggle(self.xbox, 8)

        # button for auto turn
        self.turnButtonStatus = Toggle(self.xbox, 10)   # this button status is a test for now

        # button to start shooter
        self.shooterLaunch = self.xbox.getRawAxis(3)

        # button to run intake, indexer, and semicircle
        self.intakeBall = self.xbox.getRawAxis(1)

        """ Pneumatics """
        # pneumatic compressor
        self.compressor = wpilib.Compressor(0)
        self.compressor.setClosedLoopControl(True)
        self.compressor.start()


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        """ Drive """
        # get joystick values
        self.driveLeft = self.leftJoystick.getRawAxis(1)
        self.driveRight = self.rightJoystick.getRawAxis(1)
        self.driveRotate = self.rightJoystick.getRawAxis(2)

        # changing between arcade and tank drive
        if self.driveButtonStatus.on is True:
            self.drive.tankDrive(self.driveLeft, self.driveRight)
            # sending drive train driving mode to dashboard
            self.dashboard.driveStatus('Tank Drive')

        elif self.driveButtonStatus.on is False:
            self.drive.arcadeDrive(self.driveRight, self.driveRotate)
            # sending drive train driving mode to dashboard
            self.dashboard.driveStatus('Arcade Drive')

        # changing drive train gears
        self.drive.changeGear(self.gearButtonStatus.get())
        # sending drive train gear status to dashboard
        self.dashboard.dashboardGearStatus(self.drive.getGearSolenoid())

        """ Lift """
        # run lift
        self.lift.runMotor(self.xbox.getRawButton(4))

        # changing lift state
        self.lift.changeLift(self.liftButtonStatus.get())

        # sending lift state status to dashboard
        # self.dashboard.dashboardGearStatus(self.drive.getGearSolenoid())
        # self.dashboard.dashboardLiftStatus(self.drive.getLiftSolenoid())

        """ Auto Turn w/ NavX """
        self.drive.turnToAngle(self.turnButtonStatus.get(), angle=90)

        """ Compressor """
        # self.dashboard.dashboardCompressorStatus(self.compressor.enabled())

        """ Shooter """
        self.shooter.initializeShooter(self.xbox.getRawAxis(3))

        """ Intake and Indexer"""
        # use 'forward', 'reverse', 'stop'
        if self.xbox.getPOV() == 0:
            self.intake.run('Reverse')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        elif self.xbox.getPOV() == 180:
            self.intake.run('Forward')
            self.indexer.run('Forward')
            self.semicircle.run('Forward')

        elif self.xbox.getRawButton(2) is True:
            self.intake.run('Stop')
            self.indexer.run('Forward')
            self.semicircle.run('Forward')

        else:
            self.intake.run('Stop')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        """ Auto Aim """




if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Manticore)
