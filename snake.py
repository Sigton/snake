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

        # Call the parents constructor.
        pygame.sprite.Sprite.__init__(self)

        self.snake = [ # A list of the where the snake is.
            {"x":4,"y":4},
            {"x":3,"y":4},
            {"x":2,"y":4}
            ]

        # Where the snake is pointing
        self.direction = 1 # 0=up,1=right,2=down,3=left.

        # A list of game sprites that form the snake.    
        self.snakeSegments = []

        for segment in snake:
            newSegment = GameSprite(36,36,(0,255,0))
            self.snakeSegments.append(newSegment)

    def move_next(self):

        ''' Moves the snake to the next position on the board '''

def main():

    pygame.init()

    display = (480,360)

    gameDisplay = pygame.display.set_mode(display)
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    snake = Snake

    gameExit = False

    while not gameExit:
        # Events loop
        for event in pygame.event.get():
            if event.type == QUIT:
                gameExit = True

        gameDisplay.fill((0,0,0))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
            
