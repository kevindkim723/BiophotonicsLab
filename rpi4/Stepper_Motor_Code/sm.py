import RPi.GPIO as GPIO
import time
#1 cycle = 4 steps
#1 revolution = 32 steps
#1 revolution = 8 cycles

GPIO.setmode(GPIO.BCM)

ControlPin = [0,5,6,13]
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)
#this is the matrix that defines the input to the coils within the stepper motor
half_seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]]
full_seq = [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]
def half_step():
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin],half_seq[halfstep][pin])
            time.sleep(.001)
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin],half_seq[7-halfstep][pin])
            time.sleep(.001)

    GPIO.cleanup()
def rotate():
    while (True):
        for step in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin],full_seq[step][pin])
            
            time.sleep(.009)
    GPIO.cleanup()
def main():
    try:
        GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        GPIO.add_event_detect(10, GPIO.RISING)

        while (True):
            if (GPIO.event_detected(10)):
                while (GPIO.input(10) == 1):
                    print("pressed")
                    for step in range(4):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin],full_seq[step][pin])
                                                                            time.sleep(1)
            time.sleep(.009)
    except Exception as e:
            print("Exception in pibuttons: " + e)
    finally:
            GPIO.cleanup()
if __name__ == "__main__":
    main()
