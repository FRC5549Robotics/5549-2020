""" Semicircle Functions """
import wpilib
from ctre import *

speed = 0.75

class Semicircle:
    def __init__(self):
        """ Semicircle """
        # semicircle motors
        self.semicircleMotor = WPI_TalonSRX(14)

        # reverse semicircle motor
        self.semicircleMotor.setInverted(True)

    def run(self, state):
        """ Run semicircle at set speed """
        speed = 0.75
        if state == 'Forward':
            self.semicircleMotor.set(speed)
        elif state == 'Reverse':
            self.semicircleMotor.set(-speed)
        elif state == 'Stop':
            self.semicircleMotor.set(0)