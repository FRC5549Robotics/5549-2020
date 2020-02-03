""" vision functions """
# importing packages
import wpilib
import math

class Shooter:
    __init__():
    self.heightCamera = 'int' # change later
    self.heightTarget = 'int' # change later
    self.angleMount = 'int' # change later
    self.verticalAngleToTarget = NetworkTables.getTable("limelight").getNumber('ty'); # finds vertical angle to target 
    self.horizontalAngleToTarget = NetworkTables.getTable("limelight").getNumber('tx'); # finds horizontal angle to target

    def getDistance():
        # finds distance to target using limelight
        self.distanceToTarget = (heightTarget - heightCamera) / math.tan(angleMount + angleToTarget)