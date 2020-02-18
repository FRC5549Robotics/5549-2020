""" semicircle functions """
# importing packages
import wpilib
from ctre import *

class Semicircle:
    def __init__(self):
        # semicircle motors
        self.lexanParallelMotor = WPI_Victor(9)
        self.semicircleMotor = WPI_VictorSPX(11)

    def forward(self):
        # run indexer forward
        pass

    def reverse(self):
        # run indexer reversed
        pass
