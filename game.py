#!/usr/bin/env python
import pygame

pygame.init()

screen = pygame.display.set_mode((675, 450))

background = pygame.image.load('assets/background.png')

running = True
while running:
    screen.blit(background, (0, 0))

    # Handle Events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

    pygame.display.update()
