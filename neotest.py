# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
#import board
#import neopixel

from fake_neo import FakeNeo

#pixel_pin = board.D18 # pin18
num_pixels = 10 # The number of NeoPixels
#bright = 0.1 # brightness
#ORDER = neopixel.GRB # order



def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(len(strip)):
        strip[i] = color
        strip.show()
        time.sleep(wait_ms/1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    num_pixels = len(strip)
    for _ in range (iterations):
        for q in range(3):
            for i in range(0, num_pixels, 3):
                if i+q < num_pixels:
                    strip[i+q] = color
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, num_pixels, 3):
                if i+q < num_pixels:
                    strip[i+q] = (0, 0, 0)
            


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)




def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)



pixels = FakeNeo(
    num_pixels, auto_write=False
)

colorWipe(pixels, (255, 0, 0))  # Red wipe
colorWipe(pixels, (0, 255, 0))  # Green wipe
colorWipe(pixels, (0, 0, 255))  # Blue wipe
colorWipe(pixels, (0, 0, 0))  # off
theaterChase(pixels, (255, 255, 255))  # White theater chase
theaterChase(pixels, (255, 0, 0))  # Red theater chase
theaterChase(pixels, (0, 0, 255))  # Blue theater chase
colorWipe(pixels, (0, 0, 0))  # off

print(len(pixels))


color = (0, 0, 255)
pixels.fill(color) #fill red
pixels[0] = (255, 0, 0)
pixels.show()

print(pixels[0]) #this can be used to extract current color values of a pixel

time.sleep(1)
colorWipe(pixels, (0, 0, 0))  # off


