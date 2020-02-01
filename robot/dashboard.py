''' Setting up Dashboard'''
# Importing Files
from networktables import NetworkTables

# Getting SmartDashboard
sd = NetworkTables.getTable('SmartDashboard')
NetworkTables.initialize(server='10.99.91.2')

def dashboardGearStatus(solenoidValue):
    if solenoidValue == 1:
        sd.putString("Gear Shift: ", "High Gear")
    elif solenoidValue == 2:
        sd.putString("Gear Shift: ", "Low Gear")
