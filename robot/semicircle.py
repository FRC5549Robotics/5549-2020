""" semicircle functions """
# importing packages
import wpilib
from ctre import *


class Semicircle:
    def __init__(self):
        # semicircle motors
        self.semicircleMotor = WPI_VictorSPX(14)

        # reverse semicircle motor
        self.semicircleMotor.setInverted(True)

    def forward(self):
        # run indexer forward
        # self.lexanParallelMotor.set(0.5)
        self.semicircleMotor.set(0.5)

    def reverse(self):
        # run indexer reversed
        # self.lexanParallelMotor.set(-0.5)
        self.semicircleMotor.set(-0.5)
