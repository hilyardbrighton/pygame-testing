import pygame

class Snake:
    def __init__(self, color, size, position):
        self.color = color
        self.size = size
        self.position = position
        
    def __str__(self):
        return f"Snake is currently {self.length} blocks long."
    
    def add_block(self, amount):
        self.length += amount
        
    def create_snake(self):
        snakesurface = pygame.Surface(self.size)
        snakerect = pygame.Rect(self.position,self.size)
        snake = pygame.draw.rect(snakesurface,self.color,snakerect)
        
    def snake_blit(self):
        pass
        
    