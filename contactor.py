import RPi.GPIO as GPIO
import time
from gpiozero import LED

led1 = LED(4)
led2 = LED(17)
led3 = LED(24)
led4 = LED(27)
led5 = LED(22)
led6 = LED(8)
led7 = LED(25)
led8 = LED(26)
sensor = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previous_state = False
current_state = False

while True:
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        if current_state:
            led1.off()
            led2.on()
            led3.off()
            led4.on()
            led5.off()
            led6.on()
            led7.off()
            led8.on()
        else:
            led1.on()
            led2.off()
            led3.on()
            led4.off()
            led5.on()
            led6.off()
            led7.on()
            led8.off()