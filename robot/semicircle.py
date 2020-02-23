""" semicircle functions """
# importing packages
import wpilib
from ctre import *


class Semicircle:
    def __init__(self):
        # semicircle motors
        self.semicircleMotor = WPI_TalonSRX(14)

        # reverse semicircle motor
        self.semicircleMotor.setInverted(True)

    def forward(self, run):
        # run indexer forward
        speed = 0.5
        if run is True:
            # self.lexanParallelMotor.set(speed)
            self.semicircleMotor.set(speed)
        elif run is False:
            # self.lexanParallelMotor.set(0)
            self.semicircleMotor.set(0)

    def reverse(self):
        # run indexer reversed
        # self.lexanParallelMotor.set(-0.5)
        self.semicircleMotor.set(-0.5)
