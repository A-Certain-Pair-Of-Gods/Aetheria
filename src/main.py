import pygame, sys
import settings
import map

pygame.init()

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

clock = pygame.time.Clock()

file_converter = map.TextFileTo2DArray("C:\\Users\\sylarlulu\\Documents\\Aetheria\\src\\map.txt")
file_converter.read_file()

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    file_converter.draw(screen)
    pygame.display.update()
    