import pygame

class ScrollableContainer:
    def __init__(self, width, height, content_height):
        self.WIDTH = width
        self.HEIGHT = height
        self.CONTENT_HEIGHT = content_height
        self.scroll_y = 0
        self.max_y = self.CONTENT_HEIGHT - self.HEIGHT
        self.last_scroll_time = 0

    def handle_events(self):
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                if now - self.last_scroll_time > SCROLL_COOLDOWN:
                    self.scroll_y += event.y * SCROLL_SENSITIVITY
                    self.scroll_y = max(0, min(self.scroll_y, self.max_y))
                    self.last_scroll_time = now

    def update(self):
        # Update container content and scroll bar rendering
        # Update other elements inside the container
        pass

    def draw(self, target_surface):
        # Draw container content and scroll bar onto the target surface
        bar_height = (self.HEIGHT / self.CONTENT_HEIGHT) * self.HEIGHT
        bar_y = (self.scroll_y / self.max_y) * (self.HEIGHT - bar_height)

        pygame.draw.rect(target_surface, (200, 200, 200), (0, -self.scroll_y, self.WIDTH, self.CONTENT_HEIGHT))
        pygame.draw.rect(target_surface, (150, 150, 150), (self.WIDTH - 10, bar_y, 10, bar_height))
        
    def draw_rect_alpha(self, screen, color, rect, border_radius=0):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=border_radius)
        screen.blit(shape_surf, rect)
