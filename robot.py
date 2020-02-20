"""
Infinite Recharge - Scorpio from FRC 5549: Gryphon Robotics
"""
# import packages
import wpilib
from ctre import *
from networktables import NetworkTables
from robotpy_ext.control.toggle import Toggle
from robot import *

"""
Logitech Joysticks
Left:

Right:

Xbox 360 Controller
Right Trigger(3): Shoot
A Button (1): Intake, Indexer, Semicircle

Motor Mapping
1: driveLeftMotor1
2: driveLeftMotor2
3: driveRightMotor1
4: driveRightMotor2
5: shooterTopEncoder1
6: shooterTopMotor2
7: shooterBottomEncoder1
8: shooterBottomMotor2
9: intakeMotor1
10: indexerMotor1
11: indexerMotor2
12: indexerMotor3
13: indexerMotor4
14: indexerMotor4
15: liftMotor1
"""

dashboard = Dashboard(False)
drive = Drive()
indexer = Indexer()
intake = Intake()
lift = Lift()
semicircle = Semicircle()
shooter = Shooter()
vision = Vision()

class Manticore(wpilib.TimedRobot):
    def robotInit(self):
        """ function that is run at the beginning of the match """

        # # adding functions
        # dashboard: dashboard.Dashboard
        # drive: drive.Drive
        # indexer: indexer.Indexer
        # intake: intake.Intake
        # lift: lift.Lift
        # semicircle: semicircle.Semicircle
        # shooter: shooter.Shooter
        # vision: vision.Vision

        # setting joysticks and xbox controllers
        leftJoystick = wpilib.Joystick(1)
        rightJoystick = wpilib.Joystick(2)
        xbox = wpilib.Joystick(3)  

        # get joystick values
        self.driveLeft = self.leftJoystick.getRawAxis(1)
        self.driveRight = self.rightJoystick.getRawAxis(1)
        self.driveRotate = self.leftJoystick.getRawAxis(2)

        # button for switching between arcade and tank drive
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # driving button status
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # button for gear shifting
        self.gearButtonStatus = Toggle(self.joystick, 1)

        # button to start shooter
        self.shooterLaunch = self.xbox.getRawAxis(3)

        # button to run intake, indexer, and semicircle
        self.intakeBall = self.xbox.getRawAxis(1)

    def autonomousInit(self):
        ''' function that is run at the beginning of the autonomous phase '''
        pass

    def autonomousPeriodic(self):
        ''' function that is run periodically during the autonomous phase '''
        pass

    def teleopInit(self):
        ''' function that is run at the beginning of the tele-operated phase '''
        pass

    def teleopPeriodic(self):
        ''' function that is run periodically during the tele-operated phase '''

        # changing between arcade and tank drive
        if self.driveButtonStatus.get() is True:
            self.drive.tankDrive(driveLeft, driveRight)
        else:
            self.drive.arcadeDrive(driveLeft, driveRotate)

        # changing drive train gears
        self.drive.changeGear(self.gearButtonStatus.get())

        if self.shooterLaunch is True:
            self.shooter.initializeShooter(0.5)
        else: 
            self.shooter.initializeShooter(0)

        if self.intakeBall is True:
                self.intake.takein()
                self.indexer.forward()
                self.semicircle.foward()
        else:
            pass


        'Smart Dashboard'
        self.dashboardGearStatus(self.DoubleSolenoidOne.get())


if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Manticore)
