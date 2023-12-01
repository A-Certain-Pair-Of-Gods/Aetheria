# map.py
import csv
import pygame

class Map:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.map_data = []

    def load_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.map_data = [list(map(int, row)) for row in reader]

    def draw(self, screen, camera_x, camera_y):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    # Adjust the drawing position based on the camera offset
                    draw_x = x * self.tile_size - camera_x
                    draw_y = y * self.tile_size - camera_y
                    pygame.draw.rect(screen, (0, 255, 0), (draw_x, draw_y, self.tile_size, self.tile_size))
