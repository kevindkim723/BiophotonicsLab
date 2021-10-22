import board
import neopixel
import random
pixels = neopixel.NeoPixel(board.D18, 64, brightness=.2)
while (True):
    for i in range(64):
        pixels[i] = (random.randint(0,255), random.randint(0,255),random.randint(0,255))


