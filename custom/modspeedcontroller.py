import wpilib
import ctre

import numpy as np

__all__ = ["SpeedControllerGroup_M"]

class SpeedControllerGroup_M(wpilib.SpeedControllerGroup):

    def __init__(self, *args):
        super().__init__(args[0], args[1:])
        self._driveLen = len(args)
        self.__driveCoeff = np.ones(self._driveLen)

    def setCoeffs(self, *args: float):
        corange = self._driveLen if self._driveLen < len(args) else len(args)
        for index in range(corange):
            self.__driveCoeff[index] = args[index]
        return

    def setSingleCoeff(self, index: int, term: float):
        if index+1 > self._driveLen: return
        self.__driveCoeff[index] = term
        return

    def set(self, speed: float, *args):
        for index in range(self._driveLen):
            if isinstance(self.speedControllers[index], ctre.TalonSRX):
                self.speedControllers[index].set((-speed if self.isInverted else speed)*self.__driveCoeff[index], args)
            else:
                self.speedControllers[index].set((-speed if self.isInverted else speed)*self.__driveCoeff[index])
        return

    def initSendable(self, builder):
        builder.setSmartDashboardType("Modified Speed Controller")
        builder.setSafeState(self.stopMotor)
        builder.addDoubleProperty("Value", self.get, self.set)
        return
