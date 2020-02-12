""" indexer functions """
# importing packages

from custom import SpeedControllerGroup_M
from ctre import *

class Indexer:
    def __init__(self):
        self.indexer = SpeedControllerGroup_M(WPI_VictorSPX(10), WPI_VictorSPX(11), WPI_VictorSPX(12), WPI_VictorSPX(13), WPI_VictorSPX(14))

    def forward(self):
        self.indexer.set(1.0)
        return

    def stop(self):
        self.indexer.stopMotor()
        return

    def reverse(self):
        self.indexer.set(-1)
        return