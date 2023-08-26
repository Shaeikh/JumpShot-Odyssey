import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CONTENT_HEIGHT = 1200

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Scrollable Container Example")

# Create a ScrollableContainer instance
class ScrollableContainer:
    def __init__(self, width, height, content_height):
        self.WIDTH = width
        self.HEIGHT = height
        self.CONTENT_HEIGHT = content_height
        self.SCROLL_SENSITIVITY = 100
        self.SCROLLBAR_COLOR = (150, 150, 150)
        self.SCROLLBAR_WIDTH = 10

        self.container = pygame.Surface((self.WIDTH, self.CONTENT_HEIGHT))
        self.scroll_y = 0
        self.max_y = self.CONTENT_HEIGHT - self.HEIGHT
        self.bar_height = (self.HEIGHT / self.CONTENT_HEIGHT) * self.HEIGHT

        # Initialize other attributes as needed

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEWHEEL:
                self.scroll_y -= event.y * self.SCROLL_SENSITIVITY
                self.scroll_y = max(0, min(self.scroll_y, self.max_y))

    def update(self):
        self.container.fill((255, 255, 255))
        bar_y = (self.scroll_y / self.max_y) * (self.HEIGHT - self.bar_height)

        pygame.draw.rect(self.container, (200, 200, 200), (0, -self.scroll_y, self.WIDTH, self.CONTENT_HEIGHT))
        pygame.draw.rect(self.container, self.SCROLLBAR_COLOR, (self.WIDTH - self.SCROLLBAR_WIDTH, bar_y, self.SCROLLBAR_WIDTH, self.bar_height))

    def draw(self, target_surface):
        # Draw container content and scroll bar onto the target surface
        bar_height = (self.HEIGHT / self.CONTENT_HEIGHT) * self.HEIGHT
        bar_y = (self.scroll_y / self.max_y) * (self.HEIGHT - bar_height)

        pygame.draw.rect(target_surface, (200, 200, 200), (0, -self.scroll_y, self.WIDTH, self.CONTENT_HEIGHT))
        pygame.draw.rect(target_surface, (150, 150, 150), (self.WIDTH - 10, bar_y, 10, bar_height))

# Main loop
scroll_container = ScrollableContainer(WINDOW_WIDTH, WINDOW_HEIGHT, CONTENT_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((255, 255, 255))

    # Handle events and update the scrollable container
    scroll_container.handle_events()
    scroll_container.update()

    # Draw the scrollable container onto the main window
    scroll_container.draw(window)

    pygame.display.flip()

pygame.quit()
sys.exit()
