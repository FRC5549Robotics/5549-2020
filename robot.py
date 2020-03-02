"""
Infinite Recharge - Manticore from FRC 5549: Gryphon Robotics
"""
# import packages
import wpilib
from ctre import *
from robot import *
from networktables import NetworkTables
from robotpy_ext.control.toggle import Toggle
from wpilib.drive import DifferentialDrive
import timeit

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

        # button for lift actuation
        self.liftButtonStatus = Toggle(self.xbox, 5)

        # button to run intake, indexer, and semicircle
        self.intakeBall = self.xbox.getRawAxis(1)

        # button for autoaim
        self.turnButtonStatus = self.xbox.getRawButton(6)

        """ Pneumatics """
        # pneumatic compressor
        self.compressor = wpilib.Compressor(0)
        self.compressor.setClosedLoopControl(True)
        self.compressor.start()

        """ Shooter """
        self.shooter.reset('Top')

        """" Limit Switch """
        self.limitSwitch = wpilib.DigitalInput(0)
        self.ballsInPossession = 0
        # self.lastTimeLimitSwitch = timeit.default_timer()
        self.limitSwitchTriggered = False

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.shooter.reset('Both')

    def teleopPeriodic(self):
        # shooter PID
        [self.shooterkP, self.shooterkI, self.shooterkD] = self.dashboard.getPID('Shooter')
        self.shooterkP = 0.1
        self.shooter.setPID(self.shooterkP, self.shooterkI, self.shooterkD, 'Top')

        # drive PID
        [self.drivekP, self.drivekI, self.drivekD] = self.dashboard.getPID('Drive')
        self.drive.setPID(self.drivekP, self.drivekI, self.drivekD)

        self.tx = self.dashboard.limelightDash.getNumber('tx', None)
        self.ty = self.dashboard.limelightDash.getNumber('ty', None)
        self.dashboard.limelightHorizontalAngle(self.tx)

        self.distance = self.vision.getDistance(self.ty)
        self.dashboard.distance(self.distance)

        self.navxAngle = self.drive.navx.getAngle()
        self.navxAngle = self.navxAngle % 360
        self.dashboard.navxAngle(self.navxAngle)

        # currentTime = timeit.default_timer()

        if self.limitSwitch.get() is False and self.limitSwitchTriggered is False: # and ((currentTime - self.lastTimeLimitSwitch) > 2)
            self.ballsInPossession += 1
            # self.lastTimeLimitSwitch = currentTime
            self.limitSwitchTriggered = True
        elif self.limitSwitch.get() is True:
            self.limitSwitchTriggered = False


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
        if self.lift.getLiftSolenoid() == 2:
            self.lift.runMotor(self.xbox.getRawAxis(2))

        # changing lift state
        self.lift.changeLift(self.liftButtonStatus.get())

        # sending lift state status to dashboard
        self.dashboard.dashboardLiftStatus(self.lift.getLiftSolenoid())

        """ Auto Turn w/ NavX """
        if self.xbox.getRawButton(6) is True:
            self.drive.turnToTarget(self.tx)

        """ Compressor """
        self.dashboard.dashboardCompressorStatus(self.compressor.enabled())

        """ Shooter """
        # send RPM of shooter
        self.dashboard.shooterRPMStatus(self.shooter.getShooterRPM('Top'), self.shooter.getShooterRPM('Bottom'))
        if self.xbox.getRawAxis(3) != 0:
            self.shooter.topMotors.set(self.shooter.setShooterRPM('Top', 2750))
            self.shooter.bottomMotors.set(self.shooter.setShooterRPM('Top', 2750))
            # self.shooter.bottomMotors.set(0.5)
            self.ballsInPossession = 0
        else:
            self.shooter.setShooterRPM('Stop', 0)

        """ Intake and Indexer"""
        # use 'forward', 'reverse', 'stop'
        if self.xbox.getPOV() == 0:
            self.intake.run('Reverse')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        elif self.xbox.getPOV() == 180 and self.ballsInPossession < 3:
            self.intake.run('Forward')
            self.indexer.run('Forward')
            self.semicircle.run('Forward')

        elif self.xbox.getPOV() == 180 and self.ballsInPossession >= 3:
            self.intake.run('Forward')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        else:
            self.intake.run('Stop')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        self.dashboard.ballsObtained(self.ballsInPossession)



if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Manticore)
