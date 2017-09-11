# ------------------------------------------------------------------------------------
#
# Random Walker Simulation
# Language - Python
# Modules - PyGame, sys, time
#
# By - Jatin Kumar Mandav
#
# Website - https://jatinmandav.wordpress.com
#
# YouTube Channel - https://www.youtube.com/channel/UCdpf6Lz3V357cIZomPwjuFQ
# Facebook - https://www.facebook.com/jatinmandav
# Twitter - @jatinmandav
#
# ------------------------------------------------------------------------------------

import pygame
import random
import sys

pygame.init()

width = 1000
height = 650

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Walker")

clock = pygame.time.Clock()

background = (23, 32, 42)
white = (236, 240, 241)


def walker():
    walk = True

    display.fill(background)

    posx = width/2
    posy = height/2

    w = 2
    h = 2

    steps = 0

    while walk:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        randdir = random.randrange(0, 4)

        steps += 1

        if randdir == 0:
            posy += -2
        elif randdir == 1:
            posy += 2
        elif randdir == 2:
            posx += -2
        else:
            posx += 2

        if posx > width - 10:
            posx += -3
        if posx < 10:
            posx += 3
        if posy > height - 10:
            posy += -3
        if posy < 10:
            posy += 3

        if steps == 1000:
            pygame.image.save(display, str(steps) + ".png")
        elif steps == 10000:
            pygame.image.save(display, str(steps) + ".png")
        elif steps == 50000:
            pygame.image.save(display, str(steps) + ".png")
        elif steps == 100000:
            pygame.image.save(display, str(steps) + ".png")
        elif steps == 500000:
            pygame.image.save(display, str(steps) + ".png")

        pygame.draw.rect(display, white, (posx, posy, w, h))

        pygame.display.set_caption("Random Walker : %d Steps Taken" % steps)

        pygame.display.update()
        clock.tick(60)

walker()
