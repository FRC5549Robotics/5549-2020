"""
Infinite Recharge - Manticore from FRC 5549: Gryphon Robotics
"""
import wpilib
from ctre import *
from robot import *
from networktables import NetworkTables
from robotpy_ext.control.toggle import Toggle
from wpilib.drive import DifferentialDrive
import time
from rev.color import ColorSensorV3

"""
### Motor Mapping ###
1 (Victor SPX - Positive): frontLeftMotor
2 (Victor SPX - Negative): frontRightMotor
3 (Talon SRX - Negative): rearLeftEncoder
4 (Talon SRX - Positive): rearRightEncoder
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

### Controller Mapping ###
--- Joystick ---
Right Thumb Button: change drive mode
Right Trigger: gear shift

--- Xbox ---
Left Trigger: run lift motor
Right Trigger: run shooter motor
Left Bumper: actuate lift
Right Bumper: auto align
dPAD Top: reverse intake
dPAD Bottom: runs intake + indexer + semicircle w/ color sensor
Back Button: the Oh [insert four letter string here] button
Start Button: run everything at 100% power 

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
        self.dpadForward = False
        self.dpadBackwards = False

        # button for autoaim
        self.turnButtonStatus = self.xbox.getRawButton(6)

        """ Sensors """
        # color sensor
        i2cPort = wpilib.I2C.Port.kOnboard
        self.colorSensor = ColorSensorV3(i2cPort)
        self.colorSensitivity = 180

        """ Limit Switch """
        self.limitSwitch = wpilib.DigitalInput(0)
        self.ballsInPossession = 0
        self.limitSwitchTriggered = False

        """ Pneumatics """
        # pneumatic compressor
        self.compressor = wpilib.Compressor(0)
        self.compressor.setClosedLoopControl(True)
        self.compressor.stop()

        """ Shooter """
        self.setpointReached = False
        self.shooterRun = False

        """ NavX """
        # self.drive.navx.reset()

    def autonomousInit(self):
        self.drive.rearRightEncoder.setSelectedSensorPosition(0)
        self.drive.rearLeftEncoder.setSelectedSensorPosition(0)
        self.timer = wpilib.Timer()
        self.encoderReset1 = False
        self.encoderReset2 = False
        self.encoderReset3 = False
        self.turnAngle1 = False
        self.turnAngle2 = False
        self.turnAngle3 = False
        self.firstPeriodDone = False


    def autonomousPeriodic(self):
        # timer
        self.timer.reset()
        self.timer.start()

        # limelight
        self.tx = self.dashboard.limelight('tx')

        # encoder
        self.driveTrainEncoder = (self.drive.rearLeftEncoder.getSelectedSensorPosition() + self.drive.rearRightEncoder.getSelectedSensorPosition()) / 2

        # shooter
        self.shooter.setSetpoint('Top', 2000)
        self.shooter.setSetpoint('Bottom', 2000)

        # runs between 0 and 5 seconds
        if self.timer.get() < 5:
            self.drive.turnToTarget(self.tx)
            self.shooter.execute('Top')
            self.shooter.execute('Bottom')
            if abs(self.tx) < 2:
                self.semicircle.run('Forward')

        # runs between 5 and 10
        elif 5 < self.timer.get() > 10:
            if self.firstPeriodDone == False:
                self.semicircle.run('Stop')
                self.firstPeriodDone = True
            self.shooter.setSetpoint('Top', 0)
            self.shooter.setSetpoint('Bottom', 0)
            if self.encoderReset1 == False:
                self.drive.rearRightEncoder.setSelectedSensorPosition(0)
                self.drive.rearLeftEncoder.setSelectedSensorPosition(0)
                self.encoderReset1 = True
            if self.turnAngle1 == False:
                self.drive.turnAngle(-150)
                self.turnAngle1 = True
            if self.encoderReset2 == False:
                self.drive.rearRightEncoder.setSelectedSensorPosition(0)
                self.drive.rearLeftEncoder.setSelectedSensorPosition(0)
                self.encoderReset2 = True
            self.drive.drive.tankDrive(0.5, 0.5)
            self.intake.run('Forward')
            self.indexer.run('Forward')
            self.semicircle.semicircleMotor.set(1)
            if self.driveTrainEncoder > 16384:
                self.drive.drive.stopMotor()
            else:
                pass

        # runs past 10 seconds
        if self.timer.hasPeriodPassed(10):
            if self.encoderReset3 == False:
                self.drive.rearRightEncoder.setSelectedSensorPosition(0)
                self.drive.rearLeftEncoder.setSelectedSensorPosition(0)
                self.encoderReset3 = True
            if self.turnAngle2 == False and self.encoderReset3 == True:
                self.drive.turnAngle(135)
                self.turnAngle2 = True
            if self.turnAngle3 == False and self.turnAngle2 == True:
                self.drive.turnAngle(self.tx)
                self.turnAngle3 = True
            if self.turnAngle3 == True:
                self.shooter.setSetpoint('Top', 2000)
                self.shooter.setSetpoint('Bottom', 4000)
                self.intake.run('Forward')
                self.indexer.run('Forward')
                self.semicircle.semicircleMotor.set(1)

    def teleopInit(self):
        self.drive.gearSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        # self.drive.navx.reset()
        self.drive.rearRightEncoder.setSelectedSensorPosition(0)
        self.drive.rearLeftEncoder.setSelectedSensorPosition(0)

    def teleopPeriodic(self):
        """ Updating Dashboard Values and Functions"""
        # limelight
        self.tx = self.dashboard.limelight('tx')
        self.ty = self.dashboard.limelight('ty')
        self.dashboard.limelightHorizontalAngle(self.tx)
        self.distance = self.vision.getDistance(self.ty)
        self.dashboard.distance(self.distance)

        # navx
        # self.navxAngle = self.drive.navx.getAngle()
        # self.navxAngle = self.navxAngle % 360
        # self.dashboard.navxAngle(self.navxAngle)

        # proximity sensor
        self.colorSensorProximity = self.colorSensor.getProximity()
        self.dashboard.colorSensor(self.colorSensorProximity)
        self.dashboard.ballsObtained(self.ballsInPossession)

        # send RPM of shooter
        self.dashboard.shooterRPMStatus(self.shooter.getShooterRPM('Top'), self.shooter.getShooterRPM('Bottom'))

        # gear status
        self.dashboard.gearStatus(self.drive.gearSolenoid.get()) 

        # auto align status
        self.dashboard.autoAlign()
        self.dashboard.autoRPM(self.setpointReached)

        # turns limit switch on or off based on dashboard status
        if self.dashboard.limitSwitchToggle is True:
            self.limitSwitch.start()
        elif self.dashboard.limitSwitchToggle is False:
            self.limitSwitch.stop()

        # set shooter PID
        # self.shooter.setVarPID(self.dashboard.getTestValues('P Top'), self.dashboard.getTestValues('I Top'), self.dashboard.getTestValues('D Top'), self.dashboard.getTestValues('F Top'), 'Top')
        # self.shooter.setVarPID(self.dashboard.getTestValues('P Bottom'), self.dashboard.getTestValues('I Bottom'), self.dashboard.getTestValues('D Bottom'), self.dashboard.getTestValues('F Bottom'), 'Bottom')
        # self.shooter.setPID('Top')
        # self.shooter.setPID('Bottom')

        # drive train encoders
        # self.driveTrainEncoder = (self.drive.rearLeftEncoder.getSelectedSensorPosition() + self.drive.rearRightEncoder.getSelectedSensorPosition()) / 2
        # self.dashboard.putDiagnosticValues('Drive Train Left Encoder', self.drive.rearLeftEncoder.getSelectedSensorPosition())
        # self.dashboard.putDiagnosticValues('Drive Train Right Encoder', self.drive.rearRightEncoder.getSelectedSensorPosition())
        # self.dashboard.putDiagnosticValues('Drive Train Encoder', self.driveTrainEncoder)

        # sending lift state status to dashboard
        self.dashboard.dashboardLiftStatus(self.lift.getLiftSolenoid())

        # compressor status
        # self.dashboard.dashboardCompressorStatus(self.compressor.enabled())

        # shooter rpm
        self.shooterRPMTop = (abs(self.shooter.getShooterRPM('Top')))
        self.shooterRPMBottom = (abs(self.shooter.getShooterRPM('Bottom')))


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
            self.drive.arcadeDrive(self.driveRight, self.driveRotate)
            # sending drive train driving mode to dashboard
            self.dashboard.driveStatus('Arcade Drive')

        elif self.driveButtonStatus.on is False:
            self.drive.tankDrive(self.driveLeft, self.driveRight)
            # sending drive train driving mode to dashboard
            self.dashboard.driveStatus('Tank Drive')

        # changing drive train gears
        self.drive.changeGear(self.gearButtonStatus.get())


        """ Lift """
        # changing lift state
        self.lift.changeLift(self.liftButtonStatus.get())

        # only runs lift if up
        if self.lift.getLiftSolenoid() == 2:
            self.lift.runMotor(self.xbox.getRawAxis(2))


        """ Shooter """
        # sets shooter at a certain RPM if the trigger is being pressed
        self.targetRPMTop = self.dashboard.getTestValues('RPM Top')
        self.targetRPMBottom = self.dashboard.getTestValues('RPM Bottom')
        # if self.distance < 170:
        #     self.targetRPMTop = 3759 + (-22.3 * self.distance) + (0.0576 * (self.distance * self.distance))
        # elif self.distance > 170:
        #     self.targetRPMTop = -3330 + (46.1 * self.distance) + (-0.101 * (self.distance * self.distance))
        # self.targetRPMTop = 1000
        # self.targetRPMBottom = 2000
        self.targetRPMBottom = self.targetRPMTop * 2
        self.setpointReached = False
        self.shooter.setSetpoint('Top', self.targetRPMTop)
        self.shooter.setSetpoint('Bottom', self.targetRPMBottom)
        if self.shooterLaunch > 0.25:
            self.shooterRun = True
            self.shooter.execute('Top')
            self.shooter.execute('Bottom')
            self.ballsInPossession = 0
            error = 100
            if (self.targetRPMTop - error) <= self.shooterRPMTop <= (self.targetRPMTop + error) and (self.targetRPMBottom - error) <= self.shooterRPMBottom <= (self.targetRPMBottom + error) and self.setpointReached is False:
                self.setpointReached = True
            else:
                self.setpointReached = False
        else:
            self.shooterRun = False
            self.shooter.topMotors.set(0)
            self.shooter.bottomMotors.set(0)


        """ Intake, Indexer, and Semicircle """
        # checks for amount of balls in semicircle
        if self.limitSwitch.get() is False and self.limitSwitchTriggered is False:
            self.ballsInPossession += 1
            self.limitSwitchTriggered = True
        elif self.limitSwitch.get() is True:
            self.limitSwitchTriggered = False

        # changes variables if being set to certain values
        if self.dpad == 315 or self.dpad == 0 or self.dpad == 45:
            self.dpadForward = True
        else:
            self.dpadForward = False

        if self.dpad == 135 or self.dpad == 180 or self.dpad == 225:
            self.dpadBackwards = True
        else:
            self.dpadBackwards = False

        # uses 'forward', 'reverse', 'stop'
        if self.dpadForward is True:
            # ejects balls from intake
            self.intake.run('Reverse')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        elif self.dpadBackwards is True:
            if self.colorSensorProximity >= self.colorSensitivity:
                # runs if a ball is detected
                self.intake.run('Forward')
                self.indexer.run('Forward')
                self.semicircle.run('Forward')

            elif self.colorSensorProximity < self.colorSensitivity and self.ballsInPossession < 3:
                # runs if ball is not detected
                self.intake.run('Forward')
                self.indexer.run('Forward')
                self.semicircle.run('Stop')

            elif self.ballsInPossession >= 3:
                # runs intake only if there are three or more balls in the semicircle
                self.intake.run('Forward')
                self.indexer.run('Stop')
                self.semicircle.run('Stop')

        elif self.shooterRun is True and self.setpointReached is False:
            self.intake.run('Forward')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        elif self.setpointReached is True:
            # runs if the target rpm is reached
            self.intake.run('Forward')
            self.indexer.run('Forward')
            self.semicircle.run('Forward')

        elif self.xbox.getRawButton(7) is True:
            # the oh [insert four letter string] here
            self.intake.intakeMotor.set(-1)
            self.indexer.indexer.set(-1)
            self.semicircle.semicircleMotor.set(-1)

        else:
            self.intake.run('Stop')
            self.indexer.run('Stop')
            self.semicircle.run('Stop')

        """ Auto Turn """
        if self.xbox.getRawButton(6) is True:
            self.drive.changeGear(False)
            self.drive.turnToTarget(self.tx)
            # if self.drive.resetAngle == True:
            #     self.drive.reset()
            # self.drive.turnAngle(self.tx)
            # if self.drive.resetAngle == True:
            #     self.drive.reset()
            # old navx code
            # self.drive.turnToTarget(self.tx)
            # self.targetAngle = (abs(self.drive.navx.getAngle()) % 360) + self.tx
            # self.drive.setSetpoint(self.targetAngle)
            # self.drive.execute()

if __name__ == '__main__':
    wpilib.run(Manticore)
