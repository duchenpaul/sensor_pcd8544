import time
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.OUT)


def backlight_ctrl(brightness):
    '''brightness must have a value from 0.0 to 100.0'''
    pwm = GPIO.PWM(4, 50)  # channel=12 frequency=50Hz
    pwm.start(0)
    try:
        while True:
            pwm.ChangeDutyCycle(100 - brightness)
    except Exception as e:
        raise
    else:
        pass
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    brightness = 0
    backlight_ctrl(brightness)