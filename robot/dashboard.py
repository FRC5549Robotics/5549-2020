""" dashboard functions """
from networktables import NetworkTables
import logging


class Dashboard:
    def __init__(self):
        """ Initializing Dashboard """
        # logging
        logging.basicConfig(level=logging.DEBUG)
        
        # getting shuffleboard
        self.dashboard = NetworkTables.getTable("SmartDashboard")
        self.limelightDash = NetworkTables.getTable("limelight")

        # initializing dashboard
        NetworkTables.initialize(server='10.55.49.2')

        """ Adding necessary values """

        # shooter PID
        self.dashboard.putNumber('Shooter P Top', 0)
        self.dashboard.putNumber('Shooter I Top', 0)
        self.dashboard.putNumber('Shooter D Top', 0)
        self.dashboard.putNumber('Shooter F Top', 0)

        self.dashboard.putNumber('Shooter P Bottom', 0)
        self.dashboard.putNumber('Shooter I Bottom', 0)
        self.dashboard.putNumber('Shooter D Bottom', 0)
        self.dashboard.putNumber('Shooter F Bottom', 0)

        # drive PID
        # self.dashboard.putNumber('Drive kP', 1)
        # self.dashboard.putNumber('Drive kI', 0)
        # self.dashboard.putNumber('Drive kD', 0)

        self.dashboard.putNumber('RPM Top', 0)
        self.dashboard.putNumber('RPM Bottom', 0)

        self.dashboard.putNumber("Top Shooter RPM", 0)
        self.dashboard.putNumber("Bottom Shooter RPM", 0)

        self.dashboard.putBoolean("Limit Switch Toggle", False)
        self.dashboard.putBoolean("Distance Range", False)


    def gearStatus(self, solenoidValue):
        """ Displays high/low gear to dashboard """
        if solenoidValue == 1:
            self.dashboard.putString("Gear Status", "Low")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Status", "High")


    def liftStatus(self, solenoidValue):
        """ Display Up/Down lift state to dashboard """
        if solenoidValue == 1:
            self.dashboard.putString("Lift Status", "Up")
        elif solenoidValue == 2:
            self.dashboard.putString("Lift Status", "Down")


    def compressorStatus(self, compressorValue):
        """ Display On/Off compressor state to dashboard """
        if compressorValue == True:
            self.dashboard.putString("Compressor", "On")
        elif compressorValue is False:
            self.dashboard.putString("Compressor", "Off")


    def driveStatus(self, driveButton):
        """ Display drive mode to dashboard (tank/arcade) """
        if driveButton == 'Tank Drive':
            self.dashboard.putString("Drive Status", "Tank Drive")
        elif driveButton == 'Arcade Drive':
            self.dashboard.putString("Drive Status", "Arcade Drive")


    def shooterRPMStatus(self, TopRPM, BottomRPM):
        """ Display top and bottom shooter motor RPM to testing dashboard """
        self.dashboard.putNumber("Top Shooter RPM", TopRPM)
        self.dashboard.putNumber("Bottom Shooter RPM", BottomRPM)


    def limelight(self, value):
        """ Returns limelight values """
        if value == 'tx':
            return self.limelightDash.getNumber('tx', 0)
        elif value == 'ty':
            return self.limelightDash.getNumber('ty', 0)


    def ballsObtained(self, value):
        """ Display the number of balls obtained based on limit switch values """
        self.dashboard.putNumber("Balls Obtained", value)


    def colorSensor(self, value):
        """ Display color sensor values to testing dashboard """
        self.dashboard.putNumber("Color Sensor", value)


    def limelightHorizontalAngle(self, angle):
        """ Puts tx angle from limelight """
        if angle == None:
            pass
        else:
            self.dashboard.putNumber("Limelight tx", angle)


    def navxAngle(self, angle):
        """ Displays NavX angle """
        self.dashboard.putNumber("NavX Angle", angle)


    def distance(self, distance):
        """ Displays the distance that has been calculated from Limelight """
        if distance is not None:
            self.dashboard.putNumber("Distance", distance)
        else:
            pass

          
    def autoAlign(self):
        """ Displays status of auto-align """
        if abs(self.limelightDash.getNumber('ty', 0)) < 3:
            self.dashboard.putBoolean("Auto Align", True)


    def autoRPM(self, bool):
        """ displays status of auto rpm """
        if bool == True:
            self.dashboard.putBoolean("Auto RPM", True)
        else:
            self.dashboard.putBoolean("Auto RPM", False)


    def limitSwitchToggle(self):
        """ Allows for limit switch toggle """
        return self.dashboard.getBoolean("Limit Switch Toggle", False)

    def distanceStatus(self, bool):
        """ Allows for limit switch toggle """
        if bool is True:
            self.dashboard.getBoolean("Distance Range", True)
        else:
            self.dashboard.getBoolean("Distance Range", False)

    def limelightLed(self, bool):
        """ Allows for limit switch toggle """
        if bool is True:
            self.limelightDash.putNumber("ledMode", 3)
        else:
            self.limelightDash.putNumber("ledMode", 1)


    def getTestValues(self, var):
        """ place for test values """
        if var == 'P Top':
            return self.dashboard.getNumber('Shooter P Top', 0)
        if var == 'I Top':
            return self.dashboard.getNumber('Shooter I Top', 0)
        if var == 'D Top':
            return self.dashboard.getNumber('Shooter D Top', 0)
        if var == 'F Top':
            return self.dashboard.getNumber('Shooter F Top', 0)
        if var == 'P Bottom':
            return self.dashboard.getNumber('Shooter P Bottom', 0)
        if var == 'I Bottom':
            return self.dashboard.getNumber('Shooter I Bottom', 0)
        if var == 'D Bottom':
            return self.dashboard.getNumber('Shooter D Bottom', 0)
        if var == 'F Bottom':
            return self.dashboard.getNumber('Shooter F Bottom', 0)
        if var == 'RPM Top':
            return self.dashboard.getNumber('RPM Top', 0)
        if var == 'RPM Bottom':
            return self.dashboard.getNumber('RPM Bottom', 0)


    def putDiagnosticValues(self, var, value):
        """ place to put diagnostic values """
        if var == 'Drive Train Left Encoder':
            self.dashboard.putNumber("Drive Train Left Encoder", value)
        elif var == 'Drive Train Right Encoder':
            self.dashboard.putNumber("Drive Train Right Encoder", value)
        elif var == 'Drive Train Encoder':
            self.dashboard.putNumber("Drive Train Encoder", value)
        elif var == 'Top Shooter RPM':
            self.dashboard.putNumber("Top Shooter RPM", value)
        elif var == 'Bottom Shooter RPM':
            self.dashboard.putNumber("Bottom Shooter RPM", value)
