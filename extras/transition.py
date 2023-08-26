import pygame

class Fade:
    def __init__(self, width, height, color=(0, 0, 0), duration=1000):
        self.width = width
        self.height = height
        self.color = color
        self.duration = duration
        self.alpha = 0
        self.fade_surface = pygame.Surface((self.width, self.height))
        self.fade_surface.fill(self.color)
        self.fade_rect = self.fade_surface.get_rect()

    def start_fade_in(self):
        self.alpha = 255
        self.fade_surface.set_alpha(self.alpha)

    def start_fade_out(self):
        self.alpha = 0
        self.fade_surface.set_alpha(self.alpha)

    def update(self):
        if self.alpha > 0:
            self.alpha -= int(255 / (self.duration / pygame.time.get_ticks()))
            self.fade_surface.set_alpha(self.alpha)

    def draw(self, screen):
        screen.blit(self.fade_surface, self.fade_rect)

    def hide(self):
        self.alpha = 0
        self.fade_surface.set_alpha(self.alpha)