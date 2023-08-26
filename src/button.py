import pygame, os
import pygame.mixer


current_path = os.path.dirname(__file__)

# Color
WHITE = (232, 236, 244)
BLACK = (0, 0, 0)
EMERALD_GREEN = (0, 149, 114)
HOVER_GREEN = (1, 66, 51)


def draw_text(screen, text, font, color, x, y, shadow=False, shadow_color=BLACK):
    if shadow:
        
        text_obj = font.render(text, True, shadow_color)
        screen.blit(text_obj, (x + 2, y + 2))
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

class Button():
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font, border_radius=11, left_enlarge=0, right_enlarge=0, label=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.border_radius = border_radius
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = font
        self.left_enlarge = left_enlarge
        self.right_enlarge = right_enlarge
        self.label = label
        self.clicked = False
        self.rect = pygame.Rect(self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height)

    def draw(self, screen, center=True):
        if center:
            pygame.draw.rect(screen, self.color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
            font = self.font
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        else:
            pygame.draw.rect(screen, self.color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
            font = self.font
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x, self.y + (self.height / 2 - text.get_height() / 2)))


    def hover(self, screen, mouse_pos, label_shadow=False, label_color=WHITE, center=True):
        if center:
            if (self.x - self.left_enlarge) < mouse_pos[0] < (self.x + self.width + self.right_enlarge) and self.y < mouse_pos[1] < self.y + self.height:
                

                pygame.draw.rect(screen, self.hover_color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
                font = self.font                
                text = font.render(self.text, True, self.text_color)
                screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
                
                if label_shadow and self.label:
                    label_shadow_text = font.render("> " + self.label, True, label_color)
                    screen.blit(label_shadow_text, (self.x + self.right_enlarge + 80 + 1, self.y + (self.height / 2 - label_shadow_text.get_height() / 2) + 1))
                    label = font.render("> " + self.label, True, self.text_color)
                    screen.blit(label, (self.x + self.right_enlarge + 80 , self.y + (self.height / 2 - label.get_height() / 2)))
                
                
                return True
        else:
            if (self.x - self.left_enlarge) < mouse_pos[0] < (self.x + self.width + self.right_enlarge) and self.y < mouse_pos[1] < self.y + self.height:
                pygame.draw.rect(screen, self.hover_color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
                font = self.font
                
                text = font.render(self.text, True, self.text_color)
                screen.blit(text, (self.x, self.y + (self.height / 2 - text.get_height() / 2)))
                
                if label_shadow and self.label:
                    label_shadow_text = font.render("> " + self.label, True, label_color)
                    screen.blit(label_shadow_text, (self.x + self.right_enlarge + 80 + 1, self.y + (self.height / 2 - label_shadow_text.get_height() / 2) + 1))
                    label = font.render("> " + self.label, True, self.text_color)
                    screen.blit(label, (self.x + self.right_enlarge + 80 , self.y + (self.height / 2 - label.get_height() / 2)))
                
                return True

    def is_pressed(self, mouse_pos):
        action = False
        if self.rect.collidepoint(mouse_pos) and self.clicked == False:
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
