""" dashboard functions """
# importing packages
from networktables import NetworkTables

class Dashboard:
    def __init__(self):
        # getting shuffleboard
        self.dashboard = NetworkTables.getTable('SmartDashboard')
        NetworkTables.initialize(server='10.99.91.2')

    def dashboardGearStatus(self, solenoidValue):
        # display high/low gear to dashboard
        if solenoidValue == 1:
            self.dashboard.putString("Gear Shift", "HIGH Gear")
        elif solenoidValue == 2:
            self.dashboard.putString("Gear Shift", "LOW Gear")
