""" shooter functions """
# importing packages
import wpilib
from ctre import *


class Range:
	# contains different ranges
	rangeInWords = []

	def __init__(self, rangeInWords, topRPM, bottomRPM):
		self.rangeInWords = rangeInWords  # name of the range
		self.topRPM = topRPM  # rpm of top motors
		self.bottomRPM = bottomRPM  # rpm of bottom motors


	# adds the current object to the array of ranges
	Range.rangeInWords.append(self)


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

		# setting different ranges in words
		shooterFar = Range('far', 0, 0)
		shooterMid = Range('mid', 0, 0)
		shooterShort = Range('short', 0, 0)

	def shootPredefinedDistance(self, distanceInWords):
		""" This method will call this function with the name of the range in words
		For example, you can call shootPreDefinedDistance'far') to shoot the preset 'far' distance

		:param distanceInWords:
		:type distanceInWords: String

		:return void:
		"""

		# this loop will go through each instance made by the class
		# and will find which instance's name is equlivalent to the distanceInWords
		for instance in Range.rangeInWords:
			if instance.rangeInWords == distanceInWords:
				setTopShooterRpm(instance.topRPM)  # sets the top rpm
				setBottomShooterRpm(instance.bottomRPM)  # sets the bottom rpm

	def shootAutonomous(self, distance):
		# automatically shoot balls given distance
		pass

	def velocityToRpm(rawVelocity):
		""" This method will take in velocity and convert the velocity into rotations per minute

		:param rawVelocity:
		:type rawVelocity: float

		:return rpm:
		:rtype rpm: float
		"""
		conversionFactor = 600 / 4096
		rpm = rawVelocity * conversionFactor  # convert velocity to rpm
		return rpm

	def getTopShooterRpm(self):
		""" This method will return rpm of the top shooter speed controller group

		:return rpm:
		:rtype rpm: float
		"""

		rawVelocity = self.topShooter1Encoder.getSelectedSensorVelocity()  # get velocity from encoder
		rpm = convertVelocityToRpm(rawVelocity)  # convert to rpm
		return rpm

	def getBottomShooterRpm(self):
		""" This method will return the rpm of the bottom shooter spped controller group

		:return rpm:
		:rtype rpm: float
		"""

		rawVelocity = self.bottomShooter1Encoder.getSelectedSensorVelocity()  # get velocity
		rpm = velocityToRpm(rawVelocity)  # convert to rpm
		return rpm

	def setTopShooterRpm(self, rpm):
		self.topMotors.set(rpm)

	def setBottomShooterRpm(self, rpm):
		self.bottomMotors.set(rpm)