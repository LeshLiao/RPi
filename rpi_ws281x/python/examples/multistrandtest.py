# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from neopixel import *

# LED strip configuration:
LED_1_COUNT      = 59      # Number of LED pixels.
LED_1_PIN        = 18      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 10      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 0       # 0 or 1
#LED_1_STRIP      = ws.SK6812_STRIP_GRBW
LED_1_STRIP      = ws.WS2811_STRIP_GRB

LED_2_COUNT      = 8      # Number of LED pixels.
LED_2_PIN        = 13      # GPIO pin connected to the pixels (must support PWM! GPIO 13 or 18 on RPi 3).
LED_2_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_2_DMA        = 11      # DMA channel to use for generating signal (Between 1 and 14)
LED_2_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_2_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_2_CHANNEL    = 1       # 0 or 1
LED_2_STRIP      = ws.WS2811_STRIP_GRB

def multiColorWipe(color1, color2, wait_ms=5):
	global strip1
	global strip2
	"""Wipe color across multiple LED strips a pixel at a time."""
	for i in range(strip1.numPixels()):
		if i % 2:
			# even number
			strip1.setPixelColor(i, color1)
			strip2.setPixelColor(i / 2, color2)
			strip1.show()
			time.sleep(wait_ms/1000.0)
			strip2.show()
			time.sleep(wait_ms/1000.0)
		else:
			# odd number
			strip1.setPixelColor(i, color1)
			strip1.show()
			time.sleep(wait_ms/1000.0)
	time.sleep(1)

def blackout(strip):
	for i in range(max(strip1.numPixels(), strip1.numPixels())):
		strip.setPixelColor(i, Color(0,0,0))
		strip.show()

		
#Leotest
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)
		
		
# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel objects with appropriate configuration for each strip.
	strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)
	strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, LED_2_STRIP)

	# Intialize the library (must be called once before other functions).
	strip1.begin()
	strip2.begin()

	print ('Press Ctrl-C to quit.')

	# Black out any LEDs that may be still on for the last run
	blackout(strip1)
	blackout(strip2)

	while True:

		# Multi Color wipe animations.
		multiColorWipe(Color(255, 0, 0), Color(255, 0, 0))  # Red wipe
		multiColorWipe(Color(0, 255, 0), Color(0, 255, 0))  # Blue wipe
		multiColorWipe(Color(0, 0, 255), Color(0, 0, 255))  # Green wipe
		multiColorWipe(Color(255, 255, 255), Color(255, 255, 255))  # Composite White wipe
		multiColorWipe(Color(0, 0, 0, 0), Color(0, 0, 0))  # White wipe
		multiColorWipe(Color(255, 0, 0, 0), Color(255, 0, 0))  # Composite White + White LED wipe
		rainbow(strip2)
		rainbow(strip1)
		