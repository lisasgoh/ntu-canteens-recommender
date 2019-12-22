'''
@authors:
    Leong Jing Wen
    Lim Yu Jie
    Lisa Shannon Goh
NTU BCG Y1S1 2018-19
'''

# This file contains the code to initiate and run the NTU Food Buddy

import pygame
from packages.mouseclick_related import click


GREEN = (0,255,0)
BLUE = (0,0,255)

updateButton = None
clickedButton = None

# pygame initiation
pygame.init()

page = -1


DISPLAYSURF = pygame.display.set_mode((400,300))
fontObj = pygame.font.Font('freesansbold.ttf', 20) 
textSurfaceObj = fontObj.render('Welcome to NTU Food Buddy!', True, GREEN, BLUE) 
textRectObj = textSurfaceObj.get_rect() 
textRectObj.center = (200, 150)
DISPLAYSURF.blit(textSurfaceObj, textRectObj)   # Displays welcome poge

# Continuous mouseclick enabled for running the main programme
while True:
    page, updateButton, clickedButton = click(page, updateButton, clickedButton)