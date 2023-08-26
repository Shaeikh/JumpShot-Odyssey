import pygame, os, sys
from pygame.locals import *
from player import Player
from button import Button
from sliders import Slider


current_path = os.path.dirname(__file__)

# Constants
GAME_NAME = "Jumpshot Odyssey"
screen_width = 800
screen_height = 600
player_width = 50
player_height = 50
player_x = 20
player_y = 450
velocity = 3


# Colors
WHITE = (232, 236, 244)
BLACK = (30,30,30)
EMERALD_GREEN = (0, 149, 114)
HOVER_GREEN = (1, 66, 51)
LIGHT_WHITE = (255, 255, 255, 100)
LIGHT_BLACK = (0, 0, 0, 100)


# Initialize pygame
pygame.init()

# Create screen, set caption and icon
info = pygame.display.Info()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption(GAME_NAME)
icon = pygame.image.load(os.path.join(current_path, "assets/images/icon.png"))
pygame.display.set_icon(icon)
background = pygame.image.load(os.path.join(current_path, "assets/summer.png"))
background = pygame.transform.scale(background, (screen_width, screen_height))
screen.set_alpha(0)

clock = pygame.time.Clock()

# Sliders
music_volume_slider = Slider(
        pygame.Rect(screen_width - 230, 120, 200, 50),
        step=1,
        callback=lambda val: pygame.mixer.music.set_volume(val / 100),
        slider_color=BLACK,
        color=WHITE,
    )
music_volume_slider.value = 100
sound_effects_slider = Slider(
        pygame.Rect(screen_width - 230, 165, 200, 50),
        step=1,
        callback=lambda val: pygame.mixer.music.set_volume(val / 100),
        slider_color=BLACK,
        color=WHITE,
    )
sound_effects_slider.value = 100
master_volume_slider = Slider(
        pygame.Rect(screen_width - 230, 210, 200, 50),
        step=1,
        callback=lambda val: pygame.mixer.music.set_volume(val / 100),
        slider_color=BLACK,
        color=WHITE,
    )
master_volume_slider.value = 100

pygame.mixer.music.load(
    os.path.join(
        os.path.dirname(__file__),
        "assets/sound/bg.mp3",
    )
)
pygame.mixer.music.play(loops=-1)


# Functions
def get_font(size):
    return pygame.font.Font(os.path.join(current_path, "assets/upheavtt.ttf"), size)

def draw_text(text, font, color, x, y, shadow=False, shadow_color=BLACK):
    if shadow:
        text_obj = font.render(text, True, shadow_color)
        screen.blit(text_obj, (x + 2, y + 2))

    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

def draw_rect_alpha(screen, color, rect, border_radius=0):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=border_radius)
    screen.blit(shape_surf, rect)

def bar(text):
    pygame.draw.rect(screen, EMERALD_GREEN, pygame.Rect(0, 65, screen_width, 30))
    font = get_font(30)
    text_width = font.size(text)[0] # Get the width and height of the text
    x = screen_width / 2 - text_width / 2  # Calculate the x-coordinate for centering
    draw_text(text, font, WHITE, x, 65, True, BLACK)

def center_text_x(font_size, text):
    width = get_font(font_size).size(text)[0]
    return screen_width / 2 - width / 2

def center_screen():
     return (screen.get_size()[0] // 2, screen.get_size()[1] // 2)

def key_pressed(key):
    keys = pygame.key.get_pressed()
    if keys[key]:
        return True
    return False
    

class ScreenFade():
    def __init__(self, direction, color, speed):
        self.direction = direction
        self.color = color
        self.speed = speed
        self.fade_counter = 0
        self.fading = False  # Add a flag to track fading state

    def fade(self):
        if not self.fading:  # Check if the fading process is not active
            self.fade_counter += self.speed
            if self.direction == 1:
                pygame.draw.rect(screen, self.color, (0 - self.fade_counter, 0, screen_width, screen_height))
                pygame.draw.rect(screen, self.color, (screen_width + self.fade_counter, 0, screen_width, screen_height))
                pygame.draw.rect(screen, self.color, (0, 0 - self.fade_counter, screen_width, screen_height))
                pygame.draw.rect(screen, self.color, (0, screen_height + self.fade_counter, screen_width, screen_height))

            if self.direction == 2:
               pygame.draw.rect(screen, self.color, (0, 0, screen_width, screen_height - self.fade_counter))

            alpha = 255 - self.fade_counter
            if self.direction == 3:
                if self.fade_counter <= 255:
                    fade_in = pygame.Surface((screen_width, screen_height))
                    fade_in.fill(self.color)
                    fade_in.set_alpha(self.fade_counter)
                    screen.blit(fade_in, (0, 0))
                else:
                    self.fading = True

            if self.direction == 4:
                if self.fade_counter <= 255:
                    fade_out = pygame.Surface((screen_width, screen_height))
                    fade_out.fill(self.color)
                    fade_out.set_alpha(alpha)
                    screen.blit(fade_out, (0, 0))
                else:
                    self.fading = True

            if self.fade_counter >= screen_width:
                self.fade_counter = 0
            
    # Reset fade
    def reset(self):
        self.fade_counter = 0
        self.fading = False

# Create an instance and call the fade method
fade_out = ScreenFade(4, BLACK, 15)
       

    
# Buttons
# Back button
back_button = Button(10, screen_height - 44, 62, 30, "< Back", EMERALD_GREEN, HOVER_GREEN, WHITE, get_font(15), 10, label="Hotkey: ESC")
# Options
font = get_font(15)
y_ = 130
video_settings = Button(20, y_, 80, 30, "Video", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Video Settings")
y_ += 45
audio_settings = Button(20, y_, 80, 30, "Audio", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Audio Configurations and Settings")
y_ += 45
keyboard_settings = Button(20, y_, 80, 30, "Keyboard", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Keybinds Settings")

# Video Setting
# Resizing buttons
font = get_font(15)
y_ = 130
size_sm_button = Button(20, y_, 80, 30, "800x600", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Default size")
y_ += 45
size_md_button = Button(20, y_, 80, 30, "1024x768", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1024x768")
y_ += 45
size_xmd_button = Button(20, y_, 80, 30, "1152x864", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1152x864")
y_ += 45
size_lg_button = Button(20, y_, 80, 30, "1280x720", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1280x720")
y_ += 45
size_xl_button = Button(20, y_, 80, 30, "1920x1080", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 1920x1080")
y_ += 45
size_xxl_button = Button(20, y_, 80, 30, "2560x1440", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Change window size to 2560x1440")
y_ += 45
size_full_button = Button(20, y_, 80, 30, "Fullscreen", EMERALD_GREEN, HOVER_GREEN, WHITE, font, 10, left_enlarge=10, right_enlarge=130, label="Scaling is affected")


class GameState():
    def __init__(self, screen):
        self.state = "menu"
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fullscreen = False
        # self.slider = Slider((400, 300), (300, 20), 50, 1, 99)
        self.slider = None
        self.textbox = None     

    def main_menu(self):
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

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

        fade_out.fade()
        
        

        # Events
        if play_button.is_pressed(mouse_pos):
                fade_out.reset()
                self.state = "game"
        elif options_button.is_pressed(mouse_pos):
                fade_out.reset()
                self.state = "options"
                
        elif quit_button.is_pressed(mouse_pos):
                running = False
                pygame.quit()
                sys.exit()

    def options(self):
        
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        bar("Options")
        
        
        back_button.draw(screen)
        back_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)

        
        video_settings.draw(screen, False)
        video_settings.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        
        audio_settings.draw(screen, False)
        audio_settings.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        
        keyboard_settings.draw(screen, False)
        keyboard_settings.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)

        fade_out.fade()

        # Events
        
        if back_button.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "menu"
        if video_settings.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "video_settings"
                pygame.time.delay(100)
        elif audio_settings.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "audio_settings"
        elif keyboard_settings.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "keyboard_settings"

        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN and back_button.is_pressed(pygame.mouse.get_pos()):
        #         if self.state == "options":
        #             self.state = "menu"
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE and self.state == "options":
        #             self.state = "menu"
        # pygame.display.flip()
        
    def video_settings(self):
        self.screen.fill(BLACK)
        self.screen.blit(background, (0, 0))
        bar("Video Settings")

        back_button.draw(self.screen)
        back_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)

        # Resizing buttons
        size_sm_button.draw(self.screen, False)
        size_sm_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_sm_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
        
        size_md_button.draw(self.screen, False)
        size_md_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_md_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
        
        size_xmd_button.draw(self.screen, False)
        size_xmd_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_xmd_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((1152, 864), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
        
        size_lg_button.draw(self.screen, False)
        size_lg_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_lg_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
        
        size_xl_button.draw(self.screen, False)
        size_xl_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_xl_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()

        size_xxl_button.draw(self.screen, False)
        size_xxl_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_xxl_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((2560, 1440), pygame.RESIZABLE)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()
        
        size_full_button.draw(self.screen, False)
        size_full_button.hover(self.screen, pygame.mouse.get_pos(), True, EMERALD_GREEN, False)
        if size_full_button.is_pressed(pygame.mouse.get_pos()):
            self.screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
            self.screen.blit(background, (0, 0))
            pygame.display.flip()

        fade_out.fade()

        # Events
        if back_button.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "options"

        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if back_button.is_pressed(pygame.mouse.get_pos()):
        #             if self.state == "video_settings":
        #                 self.state = "options"

        #         if size_sm_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        #         elif size_md_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)
        #         elif size_xmd_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((1152, 864), pygame.RESIZABLE)
        #         elif size_lg_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        #         elif size_xl_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
        #         elif size_xxl_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((2560, 1440), pygame.RESIZABLE)
        #         elif size_full_button.is_pressed(pygame.mouse.get_pos()):
        #             self.screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
        #         pygame.display.flip()
                

        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE and self.state == "video_settings":
        #             self.state = "options"
            
        # pygame.display.flip()
        
    def audio_settings(self):
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        bar("Audio Settings")

        back_button.draw(screen)
        back_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)
        draw_rect_alpha(screen, LIGHT_BLACK, (10, 120, self.screen_width - 30, back_button.y - 120 - 20), 10)
        music_volume_slider.draw(screen)
        sound_effects_slider.draw(screen)
        master_volume_slider.draw(screen)



        # Slider
        # if self.slider.container_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        #     self.slider.move_slider(pygame.mouse.get_pos())
        # print(self.slider.get_value())
        # self.slider.draw(screen)
        
        y_ = 130
        draw_text("Music Volume", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 45
        draw_text("Sound Effects Volume", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 45
        draw_text("Master Volume", get_font(20), WHITE, 20, y_, True, BLACK)

        fade_out.fade()
        # Events
        if back_button.is_pressed(pygame.mouse.get_pos()):
                fade_out.reset()
                self.state = "options"

    def keyboard_settings(self):
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        bar("Keyboard Settings")

        back_button.draw(screen)
        back_button.hover(screen, pygame.mouse.get_pos(), True, EMERALD_GREEN)

        # Opacity .5 container
        
        draw_rect_alpha(screen, LIGHT_BLACK, (10, 120, self.screen_width - 30, back_button.y - 120 - 20), 10)

        # Heading
        y_ = 130
        draw_text("Movement < >", get_font(30), EMERALD_GREEN, 20, y_, True, BLACK)
        y_ += 45
        draw_text("Left", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 40
        draw_text("Right", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 40
        draw_text("Jump", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 40
        draw_text("Dash", get_font(20), WHITE, 20, y_, True, BLACK)
        y_ += 45

        fade_out.fade()
        

        # Events
        if back_button.is_pressed(pygame.mouse.get_pos()):
            fade_out.reset()
            self.state = "options"

    def events(self):
        events = pygame.event.get() 
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == VIDEORESIZE:
                self.screen_width, self.screen_height = event.size
                screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                screen.blit(background, (0, 0))
            
            
           
            elif event.type == pygame.KEYDOWN:
                # Back button event
                if event.key == pygame.K_ESCAPE:
                    if self.state == "video_settings" or self.state == "audio_settings" or self.state == "keyboard_settings":
                        self.state = "options"
                    elif self.state == "options":
                        self.state = "menu"   

            pygame.display.flip()
        
        music_volume_slider.update(events)
        sound_effects_slider.update(events)
        master_volume_slider.update(events)
                
    def state_manager(self):

        # Menu
        if self.state == "menu":
            self.main_menu()
        
        # Options
        if self.state == "options":
            self.options()
        elif self.state == "video_settings":
            self.video_settings()
        elif self.state == "audio_settings":
            self.audio_settings()
        elif self.state == "keyboard_settings":
            self.keyboard_settings()
        # Call fade_out.reset() everytime the state changes
        

        self.events()

# Main loop
game_state = GameState(screen)
running = True
big = False

while running:
    game_state.state_manager()
    clock.tick(60)
    pygame.display.flip()
    
    