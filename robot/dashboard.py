""" dashboard functions """
# importing packages
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


    def dashboardGearStatus(self, solenoidValue):
        # display high/low gear to dashboard
        if solenoidValue == 1:
            self.dashboard.putString("Gear Status", "Low")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Status", "High")


    def dashboardLiftStatus(self, solenoidValue):
        # display high/low gear to dashboard
        if solenoidValue == 1:
            self.dashboard.putString("Lift Status", "Down")
        elif solenoidValue == 2:
            self.dashboard.putString("Lift Status", "Up")


    def dashboardCompressorStatus(self, compressorValue):
        # display high/low gear to dashboard
        if compressorValue == True:
            self.dashboard.putString("Compressor", "On")
        elif compressorValue == False:
            self.dashboard.putString("Compressor", "Off")


    def driveStatus(self, driveButton):
        # display drive type to dashboard
        if driveButton == 'Tank Drive':
            self.dashboard.putString("Drive Status", "Tank Drive")
        elif driveButton == 'Arcade Drive':
            self.dashboard.putString("Drive Status", "Arcade Drive")


    def shooterRPMStatus(self, TopRPM, BottomRPM):
        self.dashboard.putNumber("Top Shooter RPM", TopRPM)
        self.dashboard.putNumber("Bottom Shooter RPM", BottomRPM)


    def limelight(self, value):
        if value == 'tx':
            return self.limelightDash.getNumber('tx', 0)
        elif value == 'ty':
            return self.limelightDash.getNumber('ty', 0)


    def ballsObtained(self, value):
        self.dashboard.putNumber("Balls Obtained", value)


    def colorSensor(self, value):
        self.dashboard.putNumber("Color Sensor", value)


    def limelightHorizontalAngle(self, angle):
        if angle == None:
            pass
        else:
            self.dashboard.putNumber("Limelight tx", angle)


    def navxAngle(self, angle):
        self.dashboard.putNumber("NavX Angle", angle)


    def distance(self, distance):
        if distance is not None:
            self.dashboard.putNumber("Distance", distance)
        else:
            pass


    def encoderAngle(self, angle):
        self.dashboard.putNumber("Encoder Angle", angle)


    def shooterPID(self, output1, output2):
        self.dashboard.putNumber("Power 1", output1)
        self.dashboard.putNumber("Power 2", output2)


    def testValues(self, var):
        # if subsystem == 'Drive':
        #     self.DrivekP = self.dashboard.getNumber('Drive kP', 0)
        #     self.DrivekI = self.dashboard.getNumber('Drive kI', 0)
        #     self.DrivekD = self.dashboard.getNumber('Drive kD', 0)
        #     return self.DrivekP, self.DrivekI, self.DrivekD

        # elif subsystem == 'Shooter':
        #     self.shooterkP = self.dashboard.getNumber('Shooter kP', 0)
        #     self.shooterkI = self.dashboard.getNumber('Shooter kI', 0)
        #     self.shooterkD = self.dashboard.getNumber('Shooter kD', 0)
        #     return self.shooterkP, self.shooterkI, self.shooterkD
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
        if var == 'Drive Train Left Encoder':
            self.dashboard.putNumber("Drive Train Left Encoder", value)
        if var == 'Drive Train Right Encoder':
            self.dashboard.putNumber("Drive Train Right Encoder", value)
        if var == 'Drive Train Encoder':
            self.dashboard.putNumber("Drive Train Encoder", value)