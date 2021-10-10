#!/usr/bin/env python
import pygame

from pygame.image import load
from pygame.transform import scale, rotate

pygame.init()

screen = pygame.display.set_mode((675, 450))

background = load('assets/background.png')

player1Img = load('assets/player1.png')
player1Img = scale(player1Img, (30, 111))

player1readyArm = load('assets/player1-ready1.png')
player1readyArm = scale(player1readyArm, (42, 30))
player1readyArm = rotate(player1readyArm, 45)

player1hitArm = load('assets/player1-hit.png')
player1hitArm = scale(player1hitArm, (60, 21))

player1x = 150

running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    # Player 1
    screen.blit(player1Img, (player1x, 200))
    screen.blit(player1readyArm, (player1x, 215))
    screen.blit(player1hitArm, (player1x + 5, 230))

    # Handle Events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    pygame.display.update()
