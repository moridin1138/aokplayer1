import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound('StarWars60.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)
