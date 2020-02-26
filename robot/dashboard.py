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

        # initializing dashboard
        NetworkTables.initialize(server='10.55.49.2')

        self.dashboard.putNumber('kP', 1)
        self.dashboard.putNumber('kI', 0)
        self.dashboard.putNumber('kD', 0)

    def dashboardGearStatus(self, solenoidValue):
        # display high/low gear to dashboard
        if solenoidValue == 1:
            self.dashboard.putString("Gear Status", "Low")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Status", "High")

    def driveStatus(self, driveButton):
        # display drive type to dashboard
        if driveButton == 'Tank Drive':
            self.dashboard.putString("Drive Status", "Tank Drive")
        elif driveButton == 'Arcade Drive':
            self.dashboard.putString("Drive Status", "Arcade Drive")

    def getPID(self):
        self.kP = self.dashboard.getNumber('kP', 0)
        self.kI = self.dashboard.getNumber('kI', 0)
        self.kD = self.dashboard.getNumber('kD', 0)
        # self.kf = self.dashboard.getNumber('kF', 0)
        return self.kP, self.kI, self.kD

    def shooterRPMStatus(self, TopRPMGetter, BottomRPMGetter):
        self.dashboard.putNumber("Top Shooter RPM", TopRPMGetter)
        self.dashboard.putNumber("Bottom Shooter RPM", BottomRPMGetter)
