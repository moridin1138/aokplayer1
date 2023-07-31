from time import sleep
import pygame 
import neopixel
import board
import threading
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import AMBER

#relay setup
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

#button setup
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#sound setup
pygame.mixer.init(48000, -16, 1, 1024)
#pygame.mixer.init()

#neopixel setup
pixel_pin = board.D10
pixel_num = 45
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness = 1, auto_write = False)
pulse = Pulse(pixels, speed = 0.1, color = AMBER, period = 3)

def soundloop(soundevent):
	while True:
		sound = pygame.mixer.Sound('StarWars60.wav')
		playing = sound.play()
		if soundevent.is_set():
			break
		while playing.get_busy():
			pygame.time.delay(100)

def animateloop(ledevent):
	while True:
		pulse.animate()
		if ledevent.is_set():
			break

# create events
soundevent = Event()
ledevent = Event()

#create threads
thread1 = threading.Thread(target=soundloop, args=(soundevent,))
thread2 = threading.Thread(target=animateloop, args=(ledevent,))

def button_callback(channel):
    	print("Button was pushed!")
	GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
	thread1.start()
	thread2.start()
	sleep(10)
	soundevent.set()
	ledevent.set()

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
