"""
Infinite Recharge - Scorpio from FRC 5549: Gryphon Robotics
"""
# import packages
import wpilib
from ctre import *
from robotpy_ext.control.toggle import Toggle
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """ function that is run at the beginning of the match """

        # setting joysticks and xbox controllers
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        self.xbox = wpilib.Joystick(2)

        # drive train motors
        self.leftMotor1 = WPI_VictorSPX(12)
        self.leftMotor2 = WPI_TalonSRX(13)
        self.rightMotor1 = WPI_VictorSPX(14)
        self.rightMotor2 = WPI_TalonSRX(15)

        # drive train motor groups
        self.leftDrive = wpilib.SpeedControllerGroup(self.leftMotor1, self.leftMotor2)
        self.rightDrive = wpilib.SpeedControllerGroup(self.rightMotor1, self.rightMotor2)

        # setting up differential drive
        self.drive = DifferentialDrive(self.leftDrive, self.rightDrive)

        self.topShooter1 = WPI_VictorSPX(1)
        self.topShooterEncoder = WPI_TalonSRX(2)
        self.bottomShooterEncoder = WPI_TalonSRX(3)
        self.bottomShooter1 = WPI_VictorSPX(4)

        self.topShooters = wpilib.SpeedControllerGroup(self.topShooter1, self.topShooterEncoder)
        self.bottomShooters = wpilib.SpeedControllerGroup(self.bottomShooter1, self.bottomShooterEncoder)

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

        self.drive.tankDrive(self.driveLeft, self.driveRight)

        self.leftDrive.set(0.5)
        self.rightDrive.set(0.5)
        self.topShooters.set(0.5)
        self.bottomShooters.set(-0.5)

if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(MyRobot)
