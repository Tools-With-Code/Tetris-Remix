import pygame
import threading
import os
from pygame import mixer
from constants import *

pygame.init()

DISPLAY = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("Tetris Remix - by Tools With Code")

BLACK = (0, 0, 0)

def PlayMusic():
    mixer.music.load(os.path.join("theme.mp3"))
    mixer.music.set_volume(0.2)
    mixer.music.play()

music = threading.Thread(target=PlayMusic)
music.start()

def Main():
    FPS = 60
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        events = pygame.event.get()

        DISPLAY.fill(BLACK)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouseclicked")
        pygame.display.update()

Main()