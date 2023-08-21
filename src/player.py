import pygame, os

current_path = os.path.dirname(__file__)


class Player(pygame.sprite.Sprite):
    def __init__(self, PosX, PosY, velocity):
        super().__init__()
        self.keys_pressed = {}
        self.velocity = velocity
        self.direction = 1
        self.default_sprite = 0.075
        self.is_moving = False
        # Moving sprites
        self.sprites = []
        self.space_pressed = False
        self.sprites.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/move_0.png")
            )
        )
        self.sprites.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/move_1.png")
            )
        )
        self.sprites.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/move_2.png")
            )
        )
        self.sprites.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/move_3.png")
            )
        )
        # Standing sprites
        self.sprites_standing = []
        self.sprites_standing.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/stand_0.png")
            )
        )
        self.sprites_standing.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/stand_1.png")
            )
        )
        self.sprites_standing.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/stand_2.png")
            )
        )
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # Jumping sprites
        self.is_jumping = False
        self.jump_speed = -10
        self.sprites_jumping = []
        self.gravity = 0.5
        self.ground_level = 380
        self.sprites_jumping.append(
            pygame.image.load(
                os.path.join(current_path, "assets/images/movement/stand_0.png")
            )
        )

        self.rect = self.image.get_rect()
        self.rect.bottomleft = [PosX, PosY]

    def animate_standing(self):
        self.current_sprite += 0.08

        if self.current_sprite >= len(self.sprites_standing):
            self.current_sprite = 0

        self.image = self.sprites_standing[int(self.current_sprite)]

    def animate_jumping(self):
        self.current_sprite += 0.08

        if self.current_sprite >= len(self.sprites_jumping):
            self.current_sprite = 0

        self.image = self.sprites_jumping[int(self.current_sprite)]

    def animate(self):
        if self.is_moving:
            self.current_sprite += self.default_sprite

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

            if self.direction == -1:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.current_sprite = 0
            self.image = self.sprites_standing[int(self.current_sprite)]

        if self.is_jumping:
            self.images = []

    def update(self, keys, screen_width):
        # Update direction if moving
        move_x = 0

        # Update the keys_pressed dictionary with the current key states
        self.keys_pressed[pygame.K_a] = keys[pygame.K_a] or keys[pygame.K_LEFT]
        self.keys_pressed[pygame.K_d] = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        self.keys_pressed[pygame.K_SPACE] = keys[pygame.K_SPACE]  # Update the space key

        if self.keys_pressed[pygame.K_a]:
            move_x -= 1
            self.direction = -1
        if self.keys_pressed[pygame.K_d]:
            move_x += 1
            self.direction = 1

        if move_x != 0:
            move_x /= 1.41

        self.rect.x += move_x * self.velocity

        self.rect.x = max(0, min(self.rect.x, screen_width - self.rect.width))

        # Update animations based on movement
        if move_x != 0:
            self.is_moving = True
        else:
            self.is_moving = False

        if keys[pygame.K_SPACE] and not self.space_pressed and not self.is_jumping:
            self.space_pressed = True
            self.is_jumping = True
            self.velocity_y = self.jump_speed

        if not keys[pygame.K_SPACE]:
            self.space_pressed = False

        if self.is_jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity

            if self.rect.y >= self.ground_level:
                self.rect.y = self.ground_level
                self.is_jumping = False
                self.velocity_y = 0

            self.animate_jumping()
        else:
            if self.is_moving:
                self.animate()
            else:
                self.animate_standing()

        # Update the image based on the direction for standing animation
        if self.direction == -1:  # If facing left
            self.image = pygame.transform.flip(self.image, True, False)
