''' import statements go at the top of the program '''
import wpilib
from ctre import *
from networktables import NetworkTables

class MyRobot(wpilib.TimedRobot):
    ''' robot program starts here '''
    def robotInit(self):
        ''' function that is run at the beginning of the match '''
        # encoders
        self.topShooter1Encoder = WPI_TalonSRX(4)
        self.topShooter2wheelEncoder = WPI_TalonSRX(5)
        self.bottomShooter1 = WPI_TalonSRX(6)
        self.bottomShooter2Encoder = WPI_TalonSRX(7)

        self.topShooters = wpilib.SpeedControllerGroup(self.topShooter1Encoder, self.topShooter2wheelEncoder)

        self.topShooter1Encoder = self.topEncoder
        self.bottomShooter2Encoder = self.bottomEncoder
        self.bottomShooters = wpilib.SpeedControllerGroup( self.bottomShooter1, self.bottomShooter2Encoder)
        # xbox
        self.xbox = wpilib.JoyStick(2)

        self.sd = NetworkTables.getTable('SmartDashboard')
        NetworkTables.initialize(server='10.99.91.2')

    def autonomousInit(self):
        ''' function that is run at the beginning of the autonomous phase '''
        pass

    def autonomousPeriodic(self):
        ''' function that is run periodically during the autonomous phase '''
        pass

    def teleopInit(self):
        ''' function that is run at the beginning of the tele-operated phase '''
        pass

    def teleopPeriodic(self):
        ''' function that is run periodically during the tele-operated phase '''

        self.topValue = self.topEncoder.getQuadraturePosition()
        self.bottomValue = self.bottomEncoder.getQuadraturePosition()

        self.sd.putNumber("Top Encoder:", self.topValue)
        self.sd.putNumber("Bottom Encoder:", self.bottomValue)

        if self.xbox.getRawButton(1):
            self.topShooters.set(0.5) 
            self.bottomShooters.set(-0.5)
        
        if self.xbox.getRawButton(4):
          self.topShooters.set(-0.5) 
          self.bottomShooters.set(0.5)


if __name__ == '__main__':
    ''' running the entire robot program '''
    wpilib.run(MyRobot)
