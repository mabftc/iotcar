from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import time

class MotorController:
	def __init__(self):
		self.__init__(3)
	def __init__(self, driveType):
		# 1 = back wheel, 2 = front wheel, 3 = all wheel
		self.driveType = driveType
		self.motorHat = Adafruit_MotorHAT(addr=0x60) # I2C object for comms w/ motor HAT
		for i in range(1, 5):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
		atexit.register(self.shutdownMotors)

	def setMotorSpeed(self, motor, speed):
		speed = self.validateSpeed(speed)
		if speed >= 0:
			self.motorHat.getMotor(motor).run(Adafruit_MotorHAT.FORWARD)
		else:
			self.motorHat.getMotor(motor).run(Adafruit_MotorHAT.BACKWARD)
		self.motorHat.getMotor(motor).setSpeed(abs(speed))

	def setSpeeds(self, speeds):
		for i in range(1, 5):
			speed = speeds[i - 1]
			speed = self.validateSpeed(speed)
			if speed >= 0:
				self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
			else:
				self.motorHat.getMotor(i).run(Adafruit_MotorHAT.BACKWARD)
			self.motorHat.getMotor(i).setSpeed(abs(speed))

	def shutdownMotors(self):
		for i in range(1, 5):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.RELEASE)

	def validateSpeed(self, speed):
		r = speed;
		speed = abs(speed)
		if speed > 255:
			r = 255
		elif speed < -255:
			r = -255
		return r
