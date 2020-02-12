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

Xbox 360 Controller

Axis Mapping

Button Mapping

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


class Scorpio(wpilib.TimedRobot):

    def robotInit(self):
        """ function that is run at the beginning of the match """

        # Button for Switching Between Arcade and Tank Drive
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # Driving Button Status
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # Button for Gear Status
        self.gearButtonStatus = Toggle(self.joystick, 1)

        # init networktables
        NetworkTables.initialize(server="10.55.49.2")

        # init variables which have wpilib objects
        self.MODdrive = Drive()
        self.MODindexer = Indexer()
        self.MODintake = Intake()
        self.MODlift = Lift()
        self.MODshooter = Shooter()
        self.MODdashboard = Dashboard()
        self.MODvision = Vision()

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
        driveLeft = self.leftJoystick.getRawAxis(1)
        driveRight = self.rightJoystick.getRawAxis(1)
        driveRotate = self.leftJoystick.getRawAxis(2)

        # Changing Between Arcade and Tank Drive
        if self.driveButtonStatus.get():
            self.drive.tankDrive(driveLeft, driveRight)
        else:
            self.drive.arcadeDrive(driveLeft, driveRotate)

        # Changing Drive Train Gears
        self.drive.changeGear(self.gearButtonStatus.get())

        'Smart Dashboard'
        self.dashboardGearStatus(self.DoubleSolenoidOne.get())


if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Scorpio)
