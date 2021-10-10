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

player1readyArm = load('assets/player1-ready.png')
player1readyArm = scale(player1readyArm, (42, 30))
player1readyArm = rotate(player1readyArm, 45)

player1hitArm = load('assets/player1-hit.png')
player1hitArm = scale(player1hitArm, (60, 21))

player1x = 150
player1hitting = False

# Player 2
player2Img = load('assets/player2.png')
player2Img = scale(player2Img, (30, 111))

player2readyArm = load('assets/player2-ready.png')
player2readyArm = scale(player2readyArm, (42, 30))
player2readyArm = rotate(player2readyArm, -45)

player2hitArm = load('assets/player2-hit.png')
player2hitArm = scale(player2hitArm, (60, 21))

player2x = 400
player2hitting = False


def move_player_1(distance):
    global player1x

    new_position = player1x + distance
    if new_position > 120 and new_position < 530 and new_position + 30 < player2x:
        player1x = new_position

def move_player_2(distance):
    global player2x

    new_position = player2x + distance
    if new_position > 120 and new_position < 530 and new_position - 30 > player1x:
        player2x = new_position


running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    # Player bodies
    screen.blit(player1Img, (player1x, 200))
    screen.blit(player2Img, (player2x, 200))

    # Player Arms
    if player1hitting:
        screen.blit(player1hitArm, (player1x + 5, 232))
    else:
        screen.blit(player1readyArm, (player1x, 215))

    if player2hitting:
        screen.blit(player2hitArm, (player2x - 35, 232))
    else:
        screen.blit(player2readyArm, (player2x - 20, 215))

    # Handle Events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()   
            exit(0)

    # Handle Keyboard input
    keys = pygame.key.get_pressed()

    # Handle player 1 input
    if keys[pygame.K_d]:
        move_player_1(2)
    if keys[pygame.K_a]:
        move_player_1(-2)

    if keys[pygame.K_SPACE]:
        player1hitting = True
    else:
        player1hitting = False

    # Handle player 2 input
    if keys[pygame.K_RIGHT]:
        move_player_2(2)
    if keys[pygame.K_LEFT]:
        move_player_2(-2)

    if keys[pygame.K_RETURN]:
        player2hitting = True
    else:
        player2hitting = False
    


    pygame.display.update()
    fpsClock.tick(FPS)
