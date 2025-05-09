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
pygame.display.set_caption("Basket Oyunu")
clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (0, 200, 0)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 0)

