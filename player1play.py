import os
import playsound 
import neopixel
import board
import threading

from adafruit_led_animation.animation.pulse import Pulse

from adafruit_led_animation.color import AMBER

pixel_pin = board.D18
pixel_num = 45
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness = 1, auto_write = False)
pulse = Pulse(pixels, speed = 0.1, color = AMBER, period = 3)

SoundFilePath = "Happy_Voice.wav"

global SoundPlaying
SoundPlaying = False

def AnimateLoop():
      global SoundPlaying
      while True:
            if SoundPlaying == True:
                print("Animation!")
                pulse.animate()
            else:
                print("NO Animation")

thread1 = threading.Thread(target=AnimateLoop)
thread1.start()

SoundPlaying = True
playsound.playsound(SoundFilePath)
SoundPlaying = False

exit()
