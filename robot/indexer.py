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


    def run(self, state):
        # run indexer forward
        speed = 0.75
        if state == 'Forward':
            self.indexer.set(speed)
        elif state == 'Reverse':
            self.indexer.set(-speed)
        elif state == 'Stop':
            self.indexer.stopMotor()