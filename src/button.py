import pygame

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
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font, font_size, border_radius=11, left_enlarge=0, right_enlarge=0, label=""):
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
        self.font_size = font_size
        self.left_enlarge = left_enlarge
        self.right_enlarge = right_enlarge
        self.label = label

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
        font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def hover(self, screen, mouse_pos, label_shadow=False, label_color=WHITE):
        if (self.x - self.left_enlarge) < mouse_pos[0] < (self.x + self.width + self.right_enlarge) and self.y < mouse_pos[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color, (self.x - self.left_enlarge, self.y, self.width + self.right_enlarge, self.height), border_radius=self.border_radius)
            font = pygame.font.Font(self.font, self.font_size)
            
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
            
            if label_shadow:
                label_shadow_text = font.render(self.label, True, label_color)
                screen.blit(label_shadow_text, (self.x + self.right_enlarge + 90 + 1, self.y + (self.height / 2 - label_shadow_text.get_height() / 2) + 1))
            label = font.render(self.label, True, self.text_color)
            screen.blit(label, (self.x + self.right_enlarge + 90 , self.y + (self.height / 2 - label.get_height() / 2)))
