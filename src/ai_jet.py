import pygame
import random

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

class AIJet:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, AI_WIDTH, AI_HEIGHT)
        self.speed = speed
        self.health = 100
        self.fire_timer = pygame.time.get_ticks()  # Timer to control firing
    
    def update(self, player_rect, screen_width, screen_height):
        # Implement AI behavior and movement logic here

        # Check if it's time to fire
        current_time = pygame.time.get_ticks()
        if current_time - self.fire_timer > 2:
            self.fire_timer = current_time
            
    
    def draw(self, screen):
        pygame.draw.rect(screen, random_color(), self.rect)
