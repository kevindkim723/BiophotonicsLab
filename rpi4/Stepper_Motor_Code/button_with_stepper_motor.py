import RPi.GPIO as GPIO
import time
#1 cycle = 4 steps
#1 revolution = 32 steps
#1 revolution = 8 cycles

GPIO.setmode(GPIO.BCM)

print("Hlello")
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
    for i in range(100000):
        for step in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin],full_seq[step][pin])
            
            time.sleep(.009)
    GPIO.cleanup()
def main():

    try:
        GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        GPIO.add_event_detect(15, GPIO.RISING) 
        GPIO.add_event_detect(14, GPIO.RISING) 

        while (True):
            if (GPIO.event_detected(15)):
                while (GPIO.input(15) == 1):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin],half_seq[halfstep][pin])
                        time.sleep(.001)
            if (GPIO.event_detected(14)):
                while (GPIO.input(14)==1):
                    for halfstep in range(8):
                        for pin in range(4):
                            GPIO.output(ControlPin[pin],half_seq[7-halfstep][pin])
                        time.sleep(.001)



    except Exception as e:
            print("Exception in pibuttons: " + e)
    finally:
            GPIO.cleanup()
if __name__ == "__main__":
    main()

