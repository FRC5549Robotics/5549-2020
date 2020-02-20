""" shooter functions """
# importing packages
import wpilib
from ctre import *

# this class will hold the variables
# shootingRangeInWords: words descriptive of where the shot would land
# topRpm: the value that the top rpm will be set to
# bottomRpm: the value that the bottom rpm will be set to
class Range:
	differentRanges = []  # contains all the objects that have been created

	def __init__(self, shootingRangeInWords, topRpm, bottomRpm):
		self.shootingRangeInWords = shootingRangeInWords  # name of the range
		self.topRpm = topRpm  # speed of top rpm
		self.bottomRpm = bottomRpm  # speed of bottom rpm

		# adds the current object to the objects that have been instantiated to "differentRanges"
		Range.differentRanges.append(self)

# main shooter class
class Shooter:
	def __init__(self):
		# shooter motors and encoders
		self.topShooter1Encoder = WPI_TalonSRX(1)
		self.topShooter2 = WPI_VictorSPX(2)
		self.bottomShooter1Encoder = WPI_TalonSRX(3)
		self.bottomShooter2 = WPI_VictorSPX(4)

		# shooter motor groups
		self.topMotors = wpilib.SpeedControllerGroup(self.topShooter1Encoder, self.topShooter2)
		self.bottomMotors = wpilib.SpeedControllerGroup(self.bottomShooter1Encoder, self.bottomShooter2)

		# different ranges in words
		# examples range instances
		shooterFar = Range('far', 0, 0)  # Set top and bottom RPMs
		shooterMid = Range('mid', 0, 0)  # Set top and bottom RPMs
		shooterShort = Range('short', 0, 0)  # Set top and bottom RPMs
	
	# call this function with the name of the range in words
	# for example, you can call shootPreDefinedLengths('far')
	def shootPreDefinedLengths(self, distanceInWords):
		""" This method will set the rpm of the motors if the range in words matches the input

		:param distanceInWords:
		:type distanceInWords: String

		:return void:
		"""

		# this loop will go through each instance made by the class and will find which instance's name is equlivalent to the distanceInWords
		for instance in Range.differentRanges:
			if instance.shootingRangeInWords == distanceInWords:
				# set rpm of motor
				setTopShooterRpm(instance.topRpm)  
				setBottomShooterRpm(instance.bottomRpm) 

	def shootAutonomous(self, distance):
		# automatically shoot balls given distance
		pass

	def convertVelocityToRpm(rawVelocity):
		""" This method will take in velocity and convert the velocity into rotations per minute

		:param rawVelocity:
		:type rawVelocity: float

		:return rpm:
		:rtype rpm: float
		"""
		
		# convert velocity to rpm
		conversionFactor = 600 / 4096
		rpm = rawVelocity * conversionFactor  
		return rpm

	def getTopShooterRpm(self):
		""" This method will return rpm of the top shooter speed controller group

		:return rpm:
		:rtype rpm: float
		"""

		rawVelocity = self.topShooter1Encoder.getSelectedSensorVelocity()  # get velocity
		rpm = convertVelocityToRpm(rawVelocity)  # convert to rpm
		return rpm

	def getBottomShooterRpm(self):
		""" This method will return the rpm of the bottom shooter spped controller group

		:return rpm:
		:rtype rpm: float
		"""

		rawVelocity = self.bottomShooter1Encoder.getSelectedSensorVelocity()  # get velocity
		rpm = convertVelocityToRpm(rawVelocity)  # conver to rpm
		return rpm

	def setTopShooterRpm(self, rpm):
		self.topMotor.set(rpm)
	
	def setBottomShooterRpm(self, rpm):
		self.bottomMotor.set(rpm)