''' import statements go at the top of the program '''
import wpilib
from ctre import *
from networktables import NetworkTables
import dashboard, drive, indexer, intake, lift, robot, shooter, vision # Importing Other Files


class MyRobot(wpilib.TimedRobot):
    ''' robot program starts here '''
    def robotInit(self):
        ''' function that is run at the beginning of the match '''
        # Initialize Classes from Other Files
        self.shooter = Shooter()
        self.drive = Drive()

        # Set Axis for Drivingdrive, indexer, intake, lift, robot, shooter, vision # Importing Other Files
        driveLeft = self.leftJoystick.getRawAxis(1)
        driveRight = self.rightJoystick.getRawAxis(1)
        driveRotate = self.leftJoystick.getRawAxis(2)

        # Button for Switching Between Arcade and Tank Drive
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # Driving Button Status
        self.driveButtonStatus = Toggle(self.leftJoystick, 2)

        # Button for Gear Status
        gearButtonStatus = Toggle(self.joystick, 1)

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
        # Changing Between Arcade and Tank Drive
        if self.driveButtonStatus.on:
            self.drive.tankDrive(driveLeft, driveRight)
        if self.driveButtonStatus.off:
            self.drive.arcadeDrive(driveLeft, driveRotate)

        # Changing Drive Train Gears
        self.drive.changeGear(gearButtonStatus.get())

        'Smart Dashboard'
        dashboardGearStatus(self.DoubleSolenoidOne.get())


if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(MyRobot)
