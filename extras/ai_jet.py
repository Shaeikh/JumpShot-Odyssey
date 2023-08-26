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










        y_ = 130
        size_sm_button = Button(20, y_, 80, 30, "800x600", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Default size")
        size_sm_button.draw(screen)
        size_sm_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_md_button = Button(20, y_, 80, 30, " 1024x768", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1024x768")
        size_md_button.draw(screen)
        size_md_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_xmd_button = Button(20, y_, 80, 30, "1152x864", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1152x864")
        size_xmd_button.draw(screen)
        size_xmd_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_lg_button = Button(20, y_, 80, 30, " 1280x720", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1280x720")
        size_lg_button.draw(screen)
        size_lg_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_xl_button = Button(20, y_, 80, 30, "  1920x1080", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1920x1080")
        size_xl_button.draw(screen)
        size_xl_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_xxl_button = Button(20, y_, 80, 30, "  2560x1440", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 2560x1440")
        size_xxl_button.draw(screen)
        size_xxl_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        y_ += 45
        size_full_button = Button(20, y_, 80, 30, "     Fullscreen", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 10, left_enlarge=10, right_enlarge=130, label="Scaling is affected")
        size_full_button.draw(screen)
        size_full_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
