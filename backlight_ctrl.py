import time
import RPi.GPIO as GPIO
from gpiozero import LED
# GPIO.setmode(GPIO.BOARD)

BACKLIGHT_CTRL_PIN = 4

GPIO.setmode(GPIO.BCM) 
GPIO.setup(BACKLIGHT_CTRL_PIN, GPIO.OUT)
led = LED(BACKLIGHT_CTRL_PIN)

def backlight_ctrl(brightness):
    '''brightness must have a value from 0.0 to 100.0'''
    pwm = GPIO.PWM(BACKLIGHT_CTRL_PIN, 50)  # channel=12 frequency=50Hz
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

def backlight_toggle(swtich):
    if swtich:
        led.off()
    else:
        led.on()



if __name__ == '__main__':
    brightness = 0
    backlight_ctrl(brightness)