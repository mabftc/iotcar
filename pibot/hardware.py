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
		for i in range(4):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
		atexit.register(self.shutdownMotors)

	def setMotorSpeed(motor, speed):
		speed = self.validateSpeed(speed)
		if speed >= 0:
			for i in range(4):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
		else:
			for i in range(4):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.BACKWARD)
		self.motorHat.getMotor(motor).setSpeed(speed)

	def setSpeeds(speeds):
		for i in range(4):
			speed = speeds[i]
			speed = self.validateSpeed(speed)
			if speed >= 0:
				self.motorHat.getMotor(i).run(Adafruit_MotorHAT.FORWARD)
			else:
				self.motorHat.getMotor(i).run(Adafruit_MotorHAT.BACKWARD)
			self.motorHat.getMotor(i).setSpeed(speed)

	def shutdownMotors(self):
		for i in range(4):
			self.motorHat.getMotor(i).run(Adafruit_MotorHAT.RELEASE)

	def validateSpeed(self, speed):
		r = speed;
		if speed > 255:
			r = 255
		elif speed < -255:
			r = -255
		return r