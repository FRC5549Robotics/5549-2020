""" dashboard functions """
# importing packages
from networktables import NetworkTables
import logging

class Dashboard:
    def __init__(self):
        # logging
        logging.basicConfig(level=logging.DEBUG)
        # getting shuffleboard
        self.dashboard = NetworkTables.getTable("SmartDashboard")

        # initializing dashboard
        NetworkTables.initialize(server='10.55.49.2')

    def dashboardGearStatus(self, solenoidValue):
        # display high/low gear to dashboard
        if solenoidValue == 1:
            self.dashboard.putString("Gear Status", "High")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Status", "Low")

    def driveStatus (self, driveButton):
        # display drive type to dashboard
        if driveButton == 'Tank Drive':
            self.dashboard.putString("Drive Status", "Tank Drive")
        elif driveButton == 'Arcade Drive':
            self.dashboard.putString("Drive Status", "Arcade Drive")
