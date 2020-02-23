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

        # creates indexer motor group
        self.indexer = wpilib.SpeedControllerGroup(self.verticalIndexerLeft, self.verticalIndexerRight, self.flatIndexer)


    def forward(self, run):
        # run indexer forward
        speed = 0.5
        if run is True:
            self.indexer.set(speed)
        elif run is False:
            self.indexer.set(0)

    def reverse(self):
        # run indexer reversed
        self.flatIndexer.set(-0.5)
        self.verticalIndexerLeft.set(-0.5)
        self.verticalIndexerLeft.set(0.5)
