"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


from strandtest import *

def handler_TagAndVelocity(unused_addr, args, TagValue, VelocityValue):
  #print("print_handler_TagAndVelocity:[{0}]:{1},{2}".format(args[0], TagValue,VelocityValue))
  if TagValue == 0:
    SetPartofColor(strip,TagValue,VelocityValue,0,7) 
  elif TagValue == 1:
    SetPartofColor(strip,TagValue,VelocityValue,7,14) 
  elif TagValue == 2:
    SetPartofColor(strip,TagValue,VelocityValue,14,21) 
  elif TagValue == 3:
    SetPartofColor(strip,TagValue,VelocityValue,21,28) 
  elif TagValue == 4:
    SetPartofColor(strip,TagValue,VelocityValue,28,35) 
  elif TagValue == 5:
    SetPartofColor(strip,TagValue,VelocityValue,35,42) 
  elif TagValue == 6:
    SetPartofColor(strip,TagValue,VelocityValue,42,49) 
  elif TagValue == 7:
    SetPartofColor(strip,TagValue,VelocityValue,49,59) 	
	
	
def handler_PitchAndVelocity(unused_addr, args, PitchValue, VelocityValue):
  #print("print_note_handler:[{0}]:{1},{2}".format(args[0], PitchValue,VelocityValue))
  if PitchValue == 36:
    SetPartofColor(strip,PitchValue,VelocityValue,0,7) 
  elif PitchValue == 37:
    SetPartofColor(strip,PitchValue,VelocityValue,7,14) 
  elif PitchValue == 38:
    SetPartofColor(strip,PitchValue,VelocityValue,14,21) 
  elif PitchValue == 39:
    SetPartofColor(strip,PitchValue,VelocityValue,21,28) 
  elif PitchValue == 68:
    SetPartofColor(strip,PitchValue,VelocityValue,28,35) 
  elif PitchValue == 69:
    SetPartofColor(strip,PitchValue,VelocityValue,35,42) 
  elif PitchValue == 70:
    SetPartofColor(strip,PitchValue,VelocityValue,42,49) 
  elif PitchValue == 71:
    SetPartofColor(strip,PitchValue,VelocityValue,49,59) 


def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="10.1.1.6", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=2346, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/PitchAndVelocity*", handler_PitchAndVelocity,"PrintValue")
  dispatcher.map("/TagAndVelocity", handler_TagAndVelocity,"PrintValue")

  initled()
  opt_parse()
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
  strip.begin()
  colorWipe(strip, Color(255, 255, 0))  # Red wipe
  
  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on(test01) {}".format(server.server_address))
  server.serve_forever()
  
  
