#!/usr/bin/env python
import pygame

from pygame.image import load
from pygame.transform import scale

pygame.init()

screen = pygame.display.set_mode((675, 450))

background = load('assets/background.png')

player1Img = scale(load('assets/player1.png'), (30, 111))
player1x = 150

running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    # Player 1
    screen.blit(player1Img, (player1x, 200))

    # Handle Events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    pygame.display.update()
