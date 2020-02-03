""" indexer functions """
# importing packages
import wpilib
from ctre import *

class Indexer:
    def __init__(self):
        self.indexerMotor1 = WPI_VictorSPX(10)
        self.indexerMotor2 = WPI_VictorSPX(11)
        self.indexerMotor3 = WPI_VictorSPX(12)
        self.indexerMotor4 = WPI_VictorSPX(13)
        self.indexerMotor5 = WPI_VictorSPX(14)

    def forward(self):
        # run indexer forward
        pass

    def reverse(self):
        # run indexer reversed
        pass
