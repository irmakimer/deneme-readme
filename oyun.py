#Kütüphaneler

import pygame 
import math
import sys
import random
import time
import os

pygame.init()

# Ekran Penceresi
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Futbol Oyunu")
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (0, 200, 0)
BLUE = (50, 100, 255)

# Görseller
player_standing = pygame.image.load('run1.png')
ball_image = pygame.image.load("futboltopu.png").convert_alpha()
ball_image = pygame.transform.scale(ball_image, (50, 50))
background_image = pygame.image.load("stadyum.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

goal_image = pygame.image.load("kale.png").convert_alpha()

# Şut animasyon görselleri
shoot_anim = [
    pygame.image.load("run2.png"),
    pygame.image.load("run3.png"),
    pygame.image.load("run4.png")
]
