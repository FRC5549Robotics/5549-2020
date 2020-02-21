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
            self.dashboard.putString("Gear Shift", "HIGH Gear")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Shift", "LOW Gear")
