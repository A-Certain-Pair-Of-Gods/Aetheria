# player.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Adjust size as needed
        self.image.fill((255, 0, 0))  # Red color for simplicity
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

        # Camera attributes
        self.camera_x = 0
        self.camera_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def set_camera(self, screen_width, screen_height, map_width, map_height):
        # Adjust the camera to follow the player
        self.camera_x = max(0, min(self.rect.x - screen_width // 2, map_width - screen_width))
        self.camera_y = max(0, min(self.rect.y - screen_height // 2, map_height - screen_height))
