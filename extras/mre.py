import pygame, os, sys
from pygame.locals import *
from button import Button

current_path = os.path.dirname(__file__)

# Constants
GAME_NAME = "Jumpshot Odyssey"
screen_width = 800
screen_height = 600


# Colors
WHITE = (232, 236, 244)
BLACK = (0, 0, 0)
EMERALD_GREEN = (0, 149, 114)
HOVER_GREEN = (1, 66, 51)
LIGHT_WHITE = (255, 255, 255, 100)
LIGHT_BLACK = (0, 0, 0, 100)


# Initialize pygame
pygame.init()

# Create screen, set caption and icon
info = pygame.display.Info()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load(os.path.join(current_path, "assets/images/icon.png"))
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# Functions
def get_font(size):
    return pygame.font.Font(None, size)

def draw_text(text, font, color, x, y, shadow=False, shadow_color=BLACK):
    if shadow:
        text_obj = font.render(text, True, shadow_color)
        screen.blit(text_obj, (x + 2, y + 2))

    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

def bar(text):
    pygame.draw.rect(screen, EMERALD_GREEN, pygame.Rect(0, 65, screen_width, 30))
    font = get_font(30)
    text_width = font.size(text)[0] # Get the width and height of the text
    x = screen_width / 2 - text_width / 2  # Calculate the x-coordinate for centering
    draw_text(text, font, WHITE, x, 65, True, BLACK)

def center_text_x(font_size, text):
    width = get_font(font_size).size(text)[0]
    return screen_width / 2 - width / 2




class GameState():
    def __init__(self, screen):
        self.state = "menu"
        self.screen = screen
        self.fullscreen = False
        # self.slider = Slider((400, 300), (300, 20), 50, 1, 99)
        self.slider = None
        self.textbox = None
        

    def main_menu(self):
        screen.fill(WHITE)

        draw_text(GAME_NAME, get_font(70), EMERALD_GREEN, center_text_x(70, GAME_NAME), 30, True, BLACK)
        

        # Buttons
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos_x = mouse_pos[0]
        mouse_pos_y = mouse_pos[1]
        font_size = 20
        font = get_font(font_size)
        text_width = font.size("Play")[0]
        x = center_text_x(font_size, "Play")
        y = screen_height / 2 - 25
        height = 40
        # Play button
        play_button = Button(x, y, 70, height, "Play", EMERALD_GREEN, HOVER_GREEN, WHITE, font)
        play_button.draw(screen)
        play_button.hover(screen, mouse_pos)

        # Options button
        text_width = font.size("Options")[0]
        x = center_text_x(font_size, "Options")
        y += 55
        options_button = Button(x, y, 100, height, "Options", EMERALD_GREEN, HOVER_GREEN, WHITE, font)
        options_button.draw(screen)
        options_button.hover(screen, mouse_pos)

        # Quit button
        text_width = font.size("Quit")[0]
        x = center_text_x(font_size, "Quit")
        y += 55
        quit_button = Button(x, y, 70, height, "Quit", EMERALD_GREEN, HOVER_GREEN, WHITE, font)
        quit_button.draw(screen)
        quit_button.hover(screen, mouse_pos)

        # Events
        if play_button.is_pressed(mouse_pos):
                self.state = "game"
        elif options_button.is_pressed(mouse_pos):
                self.state = "options"
                
        elif quit_button.is_pressed(mouse_pos):
                running = False
                pygame.quit()
                sys.exit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Resize event
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.screen_width = event.w
                self.screen_height = event.h
                screen.fill(BLACK)
                pygame.display.flip()
            
            print(event)
                


                

    def state_manager(self):

        # Menu
        if self.state == "menu":
            self.main_menu()

        self.events()

# Main loop
game_state = GameState(screen)
running = True

while running:
    game_state.state_manager()
    clock.tick(60)
    pygame.display.flip()
    
    