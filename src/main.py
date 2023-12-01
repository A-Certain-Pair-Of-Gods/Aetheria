import pygame
from player import Player
from map_tiles import Map


# map.py

# main.py

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Map Example")

# Set up clock
clock = pygame.time.Clock()

# Create player
player = Player(50, 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create map
tile_size = 32
game_map = Map(tile_size)
game_map.load_from_csv('tilemap.csv')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    player.set_camera(screen_width, screen_height, game_map.tile_size * len(game_map.map_data[0]), game_map.tile_size * len(game_map.map_data))

    # Draw the map and sprites with the camera offset
    game_map.draw(screen, player.camera_x, player.camera_y)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)


# Quit Pygame
pygame.quit()
