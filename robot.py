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
from timeit import default_timer as timer
from rev.color import ColorSensorV3

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
        """ Functions """
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

        # # color sensor
        # self.colorSensor = ColorSensorV3(port=wpilib.I2C.Port())

        """ Pneumatics """
        # pneumatic compressor
        self.compressor = wpilib.Compressor(0)
        self.compressor.setClosedLoopControl(True)
        self.compressor.start()


        """ Shooter """
        self.shooter.reset('Both')
        self.setpointReached = False


        """" Limit Switch """
        self.limitSwitch = wpilib.DigitalInput(0)
        self.ballsInPossession = 0
        self.limitSwitchTriggered = False

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        """ PIDs """
        # shooter PID
        # [self.shooterkP, self.shooterkI, self.shooterkD] = self.dashboard.getPID('Shooter')
        [self.shooterkP, self.shooterkI, self.shooterkD] = [0.1, 0.0, 0.0]
        self.shooter.setPID(self.shooterkP, self.shooterkI, self.shooterkD, 'Both')

        # drive PID
        [self.drivekP, self.drivekI, self.drivekD] = self.dashboard.getPID('Drive')
        self.drive.setPID(self.drivekP, self.drivekI, self.drivekD)

        """ Updating Dashboard Values """
        # limelight
        self.tx = self.dashboard.limelight('tx')
        self.ty = self.dashboard.limelight('ty')
        self.dashboard.limelightHorizontalAngle(self.tx)
        self.distance = self.vision.getDistance(self.ty)
        self.dashboard.distance(self.distance)

        # navx
        self.navxAngle = self.drive.navx.getAngle()
        self.navxAngle = self.navxAngle % 360
        self.dashboard.navxAngle(self.navxAngle)

        # timer
        self.time = timer()

        # color sensor
        # self.colorSensorColor = self.colorSensor.getColor()

        # proximity sensor


        """ Updating Button and Joystick Values"""
        # joystick values
        self.driveLeft = self.leftJoystick.getRawAxis(1)
        self.driveRight = self.rightJoystick.getRawAxis(1)
        self.driveRotate = self.rightJoystick.getRawAxis(2)

        # xbox
        self.shooterLaunch = self.xbox.getRawAxis(3)
        self.autoTurnButton = self.xbox.getRawButton(6)
        self.dpad = self.xbox.getPOV()

        """ Drive """
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
        # changing lift state
        self.lift.changeLift(self.liftButtonStatus.get())

        # only runs lift if up
        if self.lift.getLiftSolenoid() == 2:
            self.lift.runMotor(self.xbox.getRawAxis(2))

        # sending lift state status to dashboard
        self.dashboard.dashboardLiftStatus(self.lift.getLiftSolenoid())

        """ Compressor """
        self.dashboard.dashboardCompressorStatus(self.compressor.enabled())

        """ Shooter """
        # sets shooter at a certain RPM if the trigger is being pressed
        self.targetRPM = 2750
        self.setpointReached = False
        if self.shooterLaunch > 0.25:
            self.shooter.setShooterRPM('Both', self.targetRPM)
            self.shooterRPM = (abs(self.shooter.getShooterRPM('Top')))
            self.ballsInPossession = 0
            if self.shooterRPM >= (self.targetRPM - 100):
                if self.setpointReached is False:
                    self.setpointReached = True
                    self.intake.run('Stop')
                    self.indexer.run('Forward')
                    self.semicircle.run('Forward')

        else:
            self.shooter.setShooterRPM('Stop', 0)

        # send RPM of shooter
        self.dashboard.shooterRPMStatus(self.shooter.getShooterRPM('Top'), self.shooter.getShooterRPM('Bottom'))

        """ Intake, Indexer, and Semicrcle"""
        # checks for amount of balls in semicircle
        if self.limitSwitch.get() is False and self.limitSwitchTriggered is False:
            self.ballsInPossession += 1
            self.limitSwitchTriggered = True
        elif self.limitSwitch.get() is True:
            self.limitSwitchTriggered = False

        self.dashboard.ballsObtained(self.ballsInPossession)

        # uses 'forward', 'reverse', 'stop'
        if self.dpad == 0:
            # ejects balls from intake
            self.intake.run('Reverse')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        elif self.dpad == 180 and self.ballsInPossession < 3:
            # runs intake, indexer, and semicircle if there are less than three balls in the semicircle
            self.intake.run('Forward')
            self.indexer.run('Forward')
            self.semicircle.run('Forward')

        elif self.dpad == 180 and self.ballsInPossession >= 3:
            # runs only intake if there are three or more balls in the semicircle
            self.intake.run('Forward')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        # elif self.setpointReached is True:
        #     self.intake.run('Stop')
        #     self.indexer.run('Forward')
        #     self.semicircle.run('Forward')

        else:
            self.intake.run('Stop')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')


        """ Auto Turn w/ NavX """
        if self.autoTurnButton is True:
            self.drive.turnToTarget(self.tx)



if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(Manticore)
