""" Indexer Functions """
import wpilib
from ctre import *


class Indexer:
    def __init__(self):
        """ Indexer """
        # vertical indexer motors
        self.verticalIndexerRight = WPI_TalonSRX(9)
        # self.verticalIndexerLeft = WPI_VictorSPX(10)

        # flat indexer motor
        self.flatIndexer = WPI_TalonSRX(12)

        # inverts indexer motors
        # self.verticalIndexerLeft.setInverted(True)
        self.flatIndexer.setInverted(True)

        # creates indexer motor group
        self.indexer = wpilib.SpeedControllerGroup(self.verticalIndexerRight)

    def run(self, state):
        """ Running indexer forward or in reverse """
        speed = 0.75
        if state == 'Forward':
            self.indexer.set(speed)
            self.flatIndexer.set(1.0)
        elif state == 'Reverse':
            self.indexer.set(-speed)
            self.flatIndexer.set(-1.0)
        elif state == 'Stop':
            self.indexer.stopMotor()
            self.flatIndexer.stopMotor()