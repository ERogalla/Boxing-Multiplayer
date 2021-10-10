#!/usr/bin/env python
import pygame

pygame.init()

screen = pygame.display.set_mode((675, 450))

background = pygame.image.load('assets/background.png').convert()

running = True
while running:
    # Background
    screen.blit(background, (0, 0))
    pygame.display.update()
