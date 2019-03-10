# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import sys
sys.path.append('/home/pi/Desktop/Samba_Share/rpi_ws281x/python/')

from neopixel import *

import argparse
import signal
import sys

import LeshLib

# GPIO Test
RELAY_PIN1 = 37
RELAY_PIN2 = 40
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(RELAY_PIN1,GPIO.OUT)
#GPIO.setup(RELAY_PIN2,GPIO.OUT)

def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 16     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
#LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering
LED_STRIP      = ws.WS2812_STRIP   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

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

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def colorSetting(strip,TempNote,TempVolume):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    for i in range(TempNote):
        #strip.setPixelColor(i,Color(TempVolume,TempVolume,TempVolume))
        strip.setPixelColor(i,wheel(TempVolume*2))
    strip.show()

def colorSettingByTable(strip,TempNote,TempVolume):
    """Wipe color across display a pixel at a time."""
    #for i in range(strip.numPixels()):
    #    strip.setPixelColor(i, Color(0,0,0))
    
    colorR, colorG, colorB = LeshLib.GetColorByVolume(TempVolume)
    
    for i in range(strip.numPixels()):
        strip.setPixelColor(i,Color(colorR,colorG,colorB))
    strip.show()

def SetPartofColor(strip,TempNote,TempVolume,beginLed,EndLed):
    colorR, colorG, colorB = LeshLib.GetColorByVolume(TempVolume)
    
    for i in range(beginLed,EndLed):
        strip.setPixelColor(i,Color(colorR,colorG,colorB))
    strip.show()


def SetBreatheColor(strip,TempNote,TempVolume,beginLed,EndLed):
    if(TempVolume > 0):
        colorR, colorG, colorB = LeshLib.GetColorByVolume(TempVolume)
        DelayTime = 0.005
        TotalFrame = 64 
        strip.setBrightness(255);

        for j in range(TotalFrame,0,-1):
            tempR=int((j/TotalFrame)*float(colorR))
            tempG=int((j/TotalFrame)*float(colorG))
            tempB=int((j/TotalFrame)*float(colorB))
                
            if(j == 1):
                for i in range(beginLed,EndLed):
                    strip.setPixelColor(i,Color(0,0,0))
            else:
                for i in range(beginLed,EndLed):
                    strip.setPixelColor(i,Color(tempR,tempG,tempB))
            strip.show()
            time.sleep(DelayTime)

def SetBreatheColor_02(strip,TempNote,TempVolume,beginLed,EndLed):
    if(TempVolume > 0):
        colorR, colorG, colorB = LeshLib.GetColorByVolume(TempVolume)
        DelayTime = 0.005

        for intensity in range(255,0,-4):
            strip.setBrightness(intensity);

            if(intensity <= 4):
                for i in range(beginLed,EndLed):
                    strip.setPixelColor(i,Color(0,0,0))
            else:
                for i in range(beginLed,EndLed):
                    strip.setPixelColor(i,Color(colorR,colorG,colorB))

            strip.show()
            time.sleep(DelayTime)


def SetColorByGPIO(pin_num,TempVolume):
    if TempVolume > 0:
        GPIO.output(pin_num,True)
    else:
        GPIO.output(pin_num,False)



def GetColorByMatrix(VolumeValue):
    if VolumeValue <= 127:
        return Color(ColorMatrix[VolumeValue][0],ColorMatrix[VolumeValue][1],ColorMatrix[VolumeValue][2])
    else:
        return Color(0,0,0)

def initled():
    print ('initled')
    #opt_parse()
    # Create NeoPixel object with appropriate configuration.
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    #strip.begin()

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    opt_parse()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    while True:
        print ('Color wipe animations.')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(strip, Color(0, 0, 255))  # Green wipe
        print ('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
        print ('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)
