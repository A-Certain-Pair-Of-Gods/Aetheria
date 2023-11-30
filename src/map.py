from arrow import get
from matplotlib import dates
import pygame


class TextFileTo2DArray:
    def __init__(self, file_name, delimiter='\t'):
        self.file_name = file_name
        self.delimiter = delimiter
        self.data = None

    def read_file(self):
        try:
            with open(self.file_name, mode='r') as file:
                lines = file.readlines()
                # Split each line into a list of values based on the specified delimiter
                self.data = [line.strip().split(self.delimiter) for line in lines]
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")

    def get_data(self):
        return self.data
    
    def draw(self, surface):
        datas = self.get_data()
        for i in range(0, len(datas)):
            print(datas[i])
            for j in range(0, len(datas[i])):
                for k in range(0, len(datas[i][j])):
                
                    if datas[i][j][k] == "1":
                        pygame.draw.rect(surface, (10, 10, 10), pygame.Rect(k*7.2, i*7.2 , 7.2, 7.2))

    

    

# file_converter = TextFileTo2DArray("C:\\Users\\sylarlulu\\Documents\\Aetheria\\src\\map.txt")
# file_converter.read_file()
