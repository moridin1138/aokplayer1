import pygame 
import neopixel
import board
import threading

pygame.mixer.init(48000, -16, 1, 1024)
#pygame.mixer.init()

from adafruit_led_animation.animation.pulse import Pulse

from adafruit_led_animation.color import AMBER

pixel_pin = board.D10
pixel_num = 45
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness = 1, auto_write = False)
pulse = Pulse(pixels, speed = 0.1, color = AMBER, period = 3)

def soundloop():
	while True:
		sound = pygame.mixer.Sound('StarWars60.wav')
		playing = sound.play()
		while playing.get_busy():
			pygame.time.delay(100)

def animateloop():
	while True:
		pulse.animate()

thread1 = threading.Thread(target=soundloop)
thread1.start()

thread2 = threading.Thread(target=animateloop)
thread2.start()
