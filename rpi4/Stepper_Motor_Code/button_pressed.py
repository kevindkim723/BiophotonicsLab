import RPi.GPIO  as GPIO
import time
GPIO.setmode(GPIO.BOARD)

try:
    GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.add_event_detect(10, GPIO.RISING)

    while (True):
        if (GPIO.event_detected(10)):
            while (GPIO.input(10) == 1):
                print("pressed")


        print("waiting...")
        time.sleep(1)

except Exception as e:
	print("Exception in pibuttons: " + e)
finally:
	GPIO.cleanup()
