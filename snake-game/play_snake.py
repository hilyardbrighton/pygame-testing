import pygame
from game_utils import *
from colors import Colors
import random
import time




# --------------------------------------------- #
# --Showcase of initializing pygame's modules-- #
# -----------------individually---------------- #
# --------------------------------------------- #

# Instead of initializing all pygame modules
# automatically, you can do them manually to save
# client resources.

pygame.init()

# --------------------------------------------- #
# --------Generation of media for snake-------- #
# --------------------------------------------- #

# Creation of Surface object representing the screen
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Creation of Surface object representing
# the apple that will be collected.
apple = pygame.image.load("assets/apple.png")

# Creation of Surface object to draw snake onto
#snake = Snake(Colors.green, (100, 100), (0, 0))
#snake.create_snake()
snake = pygame.image.load("assets/placeholder.png")
snakeRect = snake.get_rect()


# Creation of Rect object representing the apple
appleRect = apple.get_rect()

# --------------------------------------------- #
# ------------Functions and Classes------------ #
# --------------------------------------------- #

# Event loop
running = True

speed = [100,0]

while running:
    
    # When a pygame event happens, it is added to
    # the event queue. This loop removes them from
    # the queue every frame and represents each with
    # the index variable 'event'.
    for event in pygame.event.get():
        
        # If the event from the queue matches the type
        # pygame.QUIT, end the loop before the next frame.
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f"Key {event.key} was pressed!")
        
    
    # To simulate classic snake movement, the snake
    # will only move every 1000 milliseconds.
    if pygame.time.get_ticks() % 1000 == 0:
        #print(pygame.time.get_ticks())
        snakeRect = snakeRect.move(speed)
        
    screen.fill(Colors.black)
    screen.blit(snake,snakeRect)
    pygame.display.flip()
        
        
    
        
pygame.quit()

        