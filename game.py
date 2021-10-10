#!/usr/bin/env python
import pygame
from pygame.image import load
from pygame.transform import scale, rotate

# Pygame Settings
pygame.init()
screen = pygame.display.set_mode((675, 450))
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# Background
background = load('assets/background.png')

# Player 1
player1Img = load('assets/player1.png')
player1Img = scale(player1Img, (30, 111))

player1readyArm = load('assets/player1-ready1.png')
player1readyArm = scale(player1readyArm, (42, 30))
player1readyArm = rotate(player1readyArm, 45)

player1hitArm = load('assets/player1-hit.png')
player1hitArm = scale(player1hitArm, (60, 21))

player1x = 150

def move_player_1(distance):
    global player1x

    new_position = player1x + distance
    if new_position > 120 and new_position < 530:
        player1x = new_position


running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    # Player 1
    screen.blit(player1Img, (player1x, 200))
    screen.blit(player1readyArm, (player1x, 215))
    screen.blit(player1hitArm, (player1x + 5, 232))

    # Handle Events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()   
            exit(0)

    # Handle Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        move_player_1(2)
    elif keys[pygame.K_a]:
        move_player_1(-2)


    pygame.display.update()
    fpsClock.tick(FPS)
