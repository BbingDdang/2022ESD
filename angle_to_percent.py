import RPi.GPIO as GPIO
import time

servoPan = 17
servoTilt = 27

def angle_to_percent(angle):
	if angle > 180 or angle < 0:
		return False
	start = 4
	end = 12.5
	ratio = (end - start)/180
	angle_as_percent = angle * ratio

	return start + angle_as_percent


if __main__ == "__main__":
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPan, GPIO.OUT)
  GPIO.setup(servoTilt, GPIO.OUT)

  pwm = GPIO.PWM(servoPan, 50)

  pwm.start(angle_to_percent(0))
  time.sleep(1)

  pwm.ChangeDutyCycle(angle_to_percent(90))
  time.sleep(1)

  pwm.ChangeDutyCycle(angle_to_percent(180))
  time.sleep(1)

  pwm.stop()
  GPIO.cleanup(servoPan)
