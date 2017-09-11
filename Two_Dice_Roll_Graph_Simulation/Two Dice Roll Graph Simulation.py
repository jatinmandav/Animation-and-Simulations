# ------------------------------------------------------------------------------------
#
# Two Dice Roll Graph Simulation
# Language - Python
# Modules - pygame, sys, random
#
# By - Jatin Kumar Mandav
#
# Website - https://jatinmandav.wordpress.com
#
# YouTube Channel - https://www.youtube.com/channel/UCdpf6Lz3V357cIZomPwjuFQ
# Facebook - https://www.facebook.com/jatinmandav
# Email - jatinmandav3@gmail.com
#
# ------------------------------------------------------------------------------------

import pygame
import sys
import random

pygame.init()

width = 800
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Simulation")
clock = pygame.time.Clock()

background = (23, 32, 42)
white = (236, 240, 241)
red = (231, 76, 60)
orange = (248, 196, 113)


def add_y_axis(font):
    zero = font.render("0", True, white)
    display.blit(zero, (100, 520))
    font_large = pygame.font.SysFont("Times New Roman", 35)
    text = font_large.render("Probability", True, white)
    text = pygame.transform.rotate(text, 90)
    display.blit(text, (40, 200))


def add_x_axis(font):
    faces = 11
    x = 120
    y = 520

    for i in range(faces):
        num = font.render(str(i+2), True, white)
        display.blit(num, (x + (i+1)*45 + 10, y))


def dice_roll():
    roll = True

    font_axis = pygame.font.SysFont("Times New Roman", 20)
    number_of_rolls = 0
    font = pygame.font.SysFont("Times New Roman", 45)

    y = 150
    h = 350

    y_axis = (100, 100, 2, 400)
    x_axis = (100, 500, 600, 2)
    w = 20

    dice = []
    faces = 11

    prob_dist = []

    for i in range(faces):
        prob_dist.append(0.0)
        dice.append([100 + w + (i+1)*(w + 25), 0, 35, 0])

    while roll:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    dice_roll()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        display.fill(background)

        add_y_axis(font_axis)
        add_x_axis(font_axis)

        number_of_rolls += 1

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        prob_dist[dice1 + dice2 - 2] += 1

        text = font.render("Number of Dice Rolls : %d" % number_of_rolls, True, white)

        display.blit(text, (160, 10))

        for i in range(faces):
            dice[i][1] = y + h*(1-(prob_dist[i]/number_of_rolls)*5)
            dice[i][3] = h*(prob_dist[i]/number_of_rolls)*5
            pygame.draw.rect(display, orange, (dice[i]))

        for i in range(faces):
            percent = font_axis.render(str(prob_dist[i]/number_of_rolls), True, red)
            display.blit(percent, (dice[i][0], dice[i][1]-25))

        pygame.draw.rect(display, red, y_axis)
        pygame.draw.rect(display, red, x_axis)

        pygame.display.update()
        clock.tick(60)

dice_roll()
