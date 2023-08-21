import pygame, sys, os
from player import Player
from ai_jet import AIJet
from button import Button



pygame.init()

info = pygame.display.Info()
# Constants
GAME_NAME = "Jumpshot Odyssey"
SCREEN_WIDTH = 800 # info.current_w
SCREEN_HEIGHT = 532 # info.current_h
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_X = 20
PLAYER_Y = 450
VELOCITY = 3
current_path = os.path.dirname(__file__)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(GAME_NAME)
icon = pygame.image.load(os.path.join(current_path, "assets/images/icon.png"))
pygame.display.set_icon(icon)
bg_dir = "assets/images/bg.jpg"
background = pygame.image.load(os.path.join(current_path, bg_dir)).convert()
menu = pygame.image.load(os.path.join(current_path, "assets/images/menu/menu.jpg")).convert()
menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# vars
level_menu = False
game_running = False
options_menu = False

moving_sprites = pygame.sprite.Group()
player = Player(PLAYER_X, PLAYER_Y, VELOCITY)
moving_sprites.add(player)

clock = pygame.time.Clock()

# Color
WHITE = (232, 236, 244)
BLACK = (0, 0, 0)
EMERALD_GREEN = (0, 149, 114)
HOVER_GREEN = (1, 66, 51)



def draw_text(text, font, color, x, y, shadow=False, shadow_color=BLACK):
    if shadow:
        
        text_obj = font.render(text, True, shadow_color)
        screen.blit(text_obj, (x + 2, y + 2))
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

def bar(text):
    pygame.draw.rect(screen, EMERALD_GREEN, pygame.Rect(0, 65, SCREEN_WIDTH, 30))
    font = pygame.font.Font(os.path.join(current_path, "assets/upheavtt.ttf"), 30)
    text_width, text_height = font.size(text)  # Get the width and height of the text
    x = SCREEN_WIDTH / 2 - text_width / 2  # Calculate the x-coordinate for centering
    draw_text(text, font, WHITE, x, 65, True, BLACK)


    


while True:
    

    # Moving player
    keys = pygame.key.get_pressed()
    if (
        keys[pygame.K_a]
        or keys[pygame.K_LEFT]
        or keys[pygame.K_d]
        or keys[pygame.K_RIGHT]
    ):
        player.animate()

    # Calculate movement vector
    # player.update(keys, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Drawing the background
    # screen.blit(background, (0, 0))
    # screen.blit(menu, (0, 0))
    screen.fill((0, 0, 0))

    font_size = 15
    font_button = os.path.join(current_path, "assets/upheavtt.ttf")
    font0 = pygame.font.Font(font_button, font_size)
    text_width, text_height = font0.size("Back")
    x = 10
    y = SCREEN_HEIGHT - 40
    height = 30
    back_button = Button(x, y, 60, height, "Back", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size, 8)    

    if level_menu:
        bar("Level Menu")
        back_button.draw(screen)
        back_button.hover(screen, pygame.mouse.get_pos())
    elif options_menu:
        bar("Options")
        back_button.draw(screen)
        back_button.hover(screen, pygame.mouse.get_pos())


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
        
        
        
        
    else:
        font = pygame.font.Font(os.path.join(current_path, "assets/upheavtt.ttf"), 70)
        text_width, text_height = font.size(GAME_NAME)
        x = SCREEN_WIDTH / 2 -  text_width / 2
        
        draw_text(GAME_NAME, font, EMERALD_GREEN, x, 30, True, WHITE)

       
        # dynamic width and height
        font_size = 20
        font_button = os.path.join(current_path, "assets/upheavtt.ttf")
        font0 = pygame.font.Font(os.path.join(current_path, "assets/upheavtt.ttf"), 20)
        text_width, text_height = font0.size("Play")
         # Drawing button in center of x axis
        x = SCREEN_WIDTH / 2 - text_width / 2
        y = SCREEN_HEIGHT / 2 - 25
        height = 40
        play_button = Button(x, y, 70, height, "Play", EMERALD_GREEN, HOVER_GREEN, WHITE, font_button, font_size)
        play_button.draw(screen)
        play_button.hover(screen, pygame.mouse.get_pos())
        
        # "options" button
        text_width, text_height = font0.size("Options")
        x = SCREEN_WIDTH / 2 - text_width / 2
        
        y += 55
        options_button = Button(x, y, 100, height, "Options", EMERALD_GREEN, HOVER_GREEN, WHITE, os.path.join(current_path, "assets/upheavtt.ttf"), 20)
        options_button.draw(screen)
        options_button.hover(screen, pygame.mouse.get_pos())

        # "quit" button
        text_width, text_height = font0.size("Quit")
        x = SCREEN_WIDTH / 2 - text_width / 2
        y += 55
        quit_button = Button(x, y, 70, height, "Quit", EMERALD_GREEN, HOVER_GREEN, WHITE, os.path.join(current_path, "assets/upheavtt.ttf"), 20)
        quit_button.draw(screen)
        quit_button.hover(screen, pygame.mouse.get_pos())

   
    if game_running:
        moving_sprites.draw(screen)
        moving_sprites.update(keys, SCREEN_WIDTH)

    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                level_menu = False
                game_running = False
                options_menu = False
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH = event.w
            SCREEN_HEIGHT = event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
            pygame.display.flip()
        # Quitting the game event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handling mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.x < pygame.mouse.get_pos()[0] < play_button.x + play_button.width and play_button.y < pygame.mouse.get_pos()[1] < play_button.y + play_button.height:
                level_menu = True
                
            if quit_button.x < pygame.mouse.get_pos()[0] < quit_button.x + quit_button.width and quit_button.y < pygame.mouse.get_pos()[1] < quit_button.y + quit_button.height:
                pygame.quit()
                sys.exit()
            if options_button.x < pygame.mouse.get_pos()[0] < options_button.x + options_button.width and options_button.y < pygame.mouse.get_pos()[1] < options_button.y + options_button.height:
                options_menu = True
            if back_button.x < pygame.mouse.get_pos()[0] < back_button.x + back_button.width and back_button.y < pygame.mouse.get_pos()[1] < back_button.y + back_button.height:
                level_menu = False
                options_menu = False

    

    # Updating display
    pygame.display.update()

    # Locking frame per secod
    clock.tick(60)
