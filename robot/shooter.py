""" shooter functions """
# importing packages
from robot.shared import *
import math
from ctre import *
from custom import *

class Shooter:
    def __init__(self):
        # shooter motors and encoders
        self.topShooterEncoder = WPI_TalonSRX(4)
        self.bottomShooterEncoder = WPI_TalonSRX(6)

        # shooter motor group
        self.motors = SpeedControllerGroup_M(WPI_TalonSRX(4), WPI_TalonSRX(5), WPI_TalonSRX(6), WPI_TalonSRX(7))

    def shootAuto(self, dist, force=False):
        if (dist < (TARGETHEIGHT-TARGETMARGINS) or dist > (TARGETHEIGHT-TARGETMARGINS)) and not force:
            # Recommended to setup networktables feedback under this conditional.
            return

        # automatically shoot balls given distance
        self.motors.set(math.sqrt(-9.81*math.pow(dist, 2)/(TARGETHEIGHT-dist)), WPI_TalonSRX.ControlMode.Velocity)