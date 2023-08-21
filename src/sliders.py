import pygame

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

class Slider():

    def __init__(surface, x, y, width, height, value, min_value, max_value, text, font):
        pygame.draw.rect(surface, GRAY, (x, y, width, height))
        
        # Calculate slider position based on value
        slider_pos = x + int((value - min_value) / (max_value - min_value) * width)
        
        pygame.draw.rect(surface, BLACK, (slider_pos, y, 5, height))
        
        text_surface = font.render(f"{text}: {value}", True, BLACK)
        surface.blit(text_surface, (x - 200, y))