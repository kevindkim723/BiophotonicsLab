#programs Adafruit Neopixel Array to show LED's extending in a spiral like pattern
import board
import neopixel
import random
import numpy as np
import time
numpixels = 64
pin_number = board.D18
pixels = neopixel.NeoPixel(pin_number, numpixels, brightness=.1) #declares neopixel object at GPIO 18


def gseq(arraysize):
    #function to return the sequence of reconstruction images
    n = int(arraysize-1)/2
    sequence = np.zeros([2, (arraysize**2)])
    sequence[0,0] = n; sequence[1,0] = n
    dx=1;dy=-1;stepx=1;stepy=-1
    counter=0;direction=1
    for i in range(1,int(arraysize**2)):
        counter+=1
        if(direction ==1):
            sequence[0,i] = sequence[0,i-1]+dx
            sequence[1,i] = sequence[1,i-1]
            if (counter==abs(stepx)):
                counter = 0; direction *= -1;
                dx*=-1; stepx*=-1;
                if stepx > 0:
                    stepx+=1
                else:
                    stepx-=1
        else:
            sequence[0,i] = sequence[0,i-1]
            sequence[1,i] = sequence[1,i-1]+dy
            if counter==np.abs(stepy):
                counter = 0; direction *= -1;
                dy*=-1; stepy*=-1;
                if stepy > 0:
                    stepy+=1
                else:
                    stepy-=1
    seq = (sequence[0,:]) * arraysize + sequence[1,:]
    return seq.astype(int)

#main code
led_indices = gseq(8)-3
print(led_indices)
while (True):
    for i in range(numpixels):
       pixels[led_indices[i]] = (255,0,0)
       time.sleep(.01)


    pixels.fill((0,0,0))
        



