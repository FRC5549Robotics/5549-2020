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
        self.verticalIndexerRight = WPI_VictorSPX(11)

    def forward(self):
        # run indexer forward
        self.flatIndexer.set(0.5)
        self.verticalIndexerLeft.set(0.5)
        self.verticalIndexerLeft.set(-0.5)

    def reverse(self):
        # run indexer reversed
        pass
