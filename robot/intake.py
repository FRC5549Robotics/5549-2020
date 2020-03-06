""" Intake Functions """
# importing packages
import wpilib
from ctre import *


class Intake:
    def __init__(self):
        # intake motor
        self.intakeMotor = WPI_TalonSRX(11)

        # reverse intake motor
        self.intakeMotor.setInverted(True)

    def run(self, state):
        """ Run intake at set speed """
        speed = 0.65
        if state == 'Forward':
            self.intakeMotor.set(speed)
        elif state == 'Reverse':
            self.intakeMotor.set(-speed)
        elif state == 'Stop':
            self.intakeMotor.set(0)
