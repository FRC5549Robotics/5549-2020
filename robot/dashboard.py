""" dashboard functions """
# importing packages
from networktables import NetworkTables
import logging


class Dashboard:
    def __init__(self):
        # adding functions
        # self.shooter = Shooter()

        """ Initializing Dashboard """
        # logging
        logging.basicConfig(level=logging.DEBUG)
        
        # getting shuffleboard
        self.dashboard = NetworkTables.getTable("SmartDashboard")
        self.limelightDash = NetworkTables.getTable("limelight")

        # initializing dashboard
        NetworkTables.initialize(server='10.55.49.2')

        # shooter PID
        self.dashboard.putNumber('Shooter kP', 1)
        self.dashboard.putNumber('Shooter kI', 0)
        self.dashboard.putNumber('Shooter kD', 0)

        # drive PID
        self.dashboard.putNumber('Drive kP', 1)
        self.dashboard.putNumber('Drive kI', 0)
        self.dashboard.putNumber('Drive kD', 0)


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


    def getPID(self, subsystem):
        if subsystem == 'Drive':
            self.DrivekP = self.dashboard.getNumber('Drive kP', 0)
            self.DrivekI = self.dashboard.getNumber('Drive kI', 0)
            self.DrivekD = self.dashboard.getNumber('Drive kD', 0)
            return self.DrivekP, self.DrivekI, self.DrivekD
    
        elif subsystem == 'Shooter':
            self.shooterkP = self.dashboard.getNumber('Shooter kP', 0)
            self.shooterkI = self.dashboard.getNumber('Shooter kI', 0)
            self.shooterkD = self.dashboard.getNumber('Shooter kD', 0)
            return self.shooterkP, self.shooterkI, self.shooterkD


    def shooterRPMStatus(self, TopRPM, BottomRPM):
        self.dashboard.putNumber("Top Shooter RPM", TopRPM)
        self.dashboard.putNumber("Bottom Shooter RPM", BottomRPM)


    def limelight(self, value):
        if value == 'tx':
            return self.limelightDash.getNumber('tx', None)
        elif value == 'ty':
            return self.limelightDash.getNumber('ty', None)


    def ballsObtained(self, value):
        self.dashboard.putNumber("Balls Obtained", value)


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