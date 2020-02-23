""" indexer functions """
# importing packages
import wpilib
from ctre import *


class Indexer:
    def __init__(self):
        # vertical indexer motors
        self.verticalIndexerRight = WPI_TalonSRX(9)
        self.verticalIndexerLeft = WPI_VictorSPX(10)

        # flat indexer motor
        self.flatIndexer = WPI_TalonSRX(12)

        # inverts indexer motors
        self.flatIndexer.setInverted(True)

    def forward(self):
        # run indexer forward
        self.flatIndexer.set(0.5)
        self.verticalIndexerLeft.set(0.5)
        self.verticalIndexerLeft.set(-0.5)

    def reverse(self):
        # run indexer reversed
        self.flatIndexer.set(-0.5)
        self.verticalIndexerLeft.set(-0.5)
        self.verticalIndexerLeft.set(0.5)
