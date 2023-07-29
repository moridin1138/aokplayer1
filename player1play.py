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

def soundloop():
      while True:
            playsound.playsound("Happy_Voice.wav")

def animateloop():
      while True:
            pulse.animate()

thread1 = threading.Thread(target=soundloop)
thread1.start()

thread2 = threading.Thread(target=animateloop)
thread2.start()
