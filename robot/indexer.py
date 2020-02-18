""" indexer functions """
# importing packages
import wpilib
from ctre import *

class Indexer:
    def __init__(self):
        # indexer motors
        self.flatIndexer = WPI_VictorSRX(7)
        # from front view
        self.verticalIndexerLeft = WPI_TalonSRX(5) 
        self.verticalIndexerRight = WPI_VictorSPX(12)

    def forward(self):
        # run indexer forward
        pass

    def reverse(self):
        # run indexer reversed
        pass
