'''
SNAKE V1
By Sigton

Snake:
Based off of a Scratch game I made recently.
'''

import pygame
from pygame.locals import *

class GameSprite(pygame.sprite.Sprite):

    ''' Basic game sprite for various uses '''

    def __init__(self, width, height, color):

        ''' Constructor '''

        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        # Create the image
        self.image = pygame.Surface([36,36]).convert()
        self.image.fill((color))
        

class Snake(pygame.sprite.Sprite):

    ''' This is the basic snake class '''

    def __init__(self):

        ''' Constructor '''

        # Call the parents constructor
        pygame.sprite.Sprite.__init__(self)

        self.snake = [ # A list of the where the snake is
            {"x":4,"y":4},
            {"x":3,"y":4},
            {"x":2,"y":4}
            ]

        self.snakeSegments = []

        for segment in snake:
            newSegment = GameSprite(36,36,(0,255,0))
            self.snakeSegments.append(newSegment)

def main():

    display = (480,360)

    gameDisplay = pygame.display.set_mode(display)
    pygame.display.set_caption("Snake")
            
