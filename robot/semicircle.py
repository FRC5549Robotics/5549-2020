""" semicircle functions """
# importing packages
import wpilib
from ctre import *


class Semicircle:
    def __init__(self):
        # semicircle motors
        self.semicircleMotor = WPI_TalonSRX(14)

        # reverse semicircle motor
        self.semicircleMotor.setInverted(True)


    def run(self, state):
        # run indexer forward
        speed = 0.70
        if state == 'Forward':
            self.semicircleMotor.set(speed)
        elif state == 'Reverse':
            self.semicircleMotor.set(-speed)
        elif state == 'Stop':
            self.semicircleMotor.set(0)