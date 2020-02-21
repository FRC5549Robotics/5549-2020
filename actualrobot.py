"""
Infinite Recharge - Scorpio from FRC 5549: Gryphon Robotics
"""
# import packages
import wpilib
from ctre import *
from networktables import NetworkTables
from robotpy_ext.control.toggle import Toggle
from wpilib.drive import DifferentialDrive

from robot import *

"""
Logitech Joysticks
Left:

Right:

Xbox 360 Controller
Right Trigger(3): Shoot
A Button (1): Intake, Indexer, Semicircle

Motor Mapping
1: topShooter1Encoder
2: topShooter2
3: bottomShooter1Encoder
4: bottomShooter2
5: verticalIndexerLeft
6: intakeMotor
7: flatIndexer
8: 
9: 
10: liftMotor
11: 
12: 
13: 
14: 
15: 
"""

class Manticore(wpilib.TimedRobot):
    def robotInit(self):
        """ function that is run at the beginning of the match """

        # adding functions
        self.dashboard = Dashboard()
        self.drive = Drive()
        self.indexer = Indexer()
        self.intake = Intake()
        self.lift = Lift()
        self.semicircle = Semicircle()
        self.shooter = Shooter()
        self.vision = Vision()

        # setting joysticks and xbox controllers
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        self.xbox = wpilib.Joystick(2)

        # button for switching between arcade and tank drive
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # driving button status
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # button for gear shifting
        self.gearButtonStatus = Toggle(self.rightJoystick, 1)

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

        # get joystick values
        self.driveLeft = self.leftJoystick.getRawAxis(1)
        self.driveRight = self.rightJoystick.getRawAxis(1)
        self.driveRotate = self.rightJoystick.getRawAxis(2)

        self.drive.tankDrive(self.driveLeft, self.driveRight)

        # # changing between arcade and tank drive
        # if self.driveButtonStatus.get() is True:
        #     Drive.tankDrive(self.drive, self.driveLeft, self.driveRight)
        # else:
        #     Drive.arcadeDrive(self.drive, self.driveLeft, self.driveRotate)

        # changing drive train gears
        Drive.changeGear(self.drive, self.gearButtonStatus.get())

        # if self.shooterLaunch is True:
        #     Shooter.initializeShooter(0.5)
        # else:
        #     Shooter.initializeShooter(0)
        #
        # if self.intakeBall is True:
        #         Intake.takein()
        #         Indexer.forward()
        #         Semicircle.forward()
        # else:
        #     pass


        # self.dashboardGearStatus(self.DoubleSolenoidOne.get())


if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Manticore)
