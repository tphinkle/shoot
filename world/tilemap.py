# Scipy
import numpy as np

# Game dependent
import tile

class TileMap():
    def __init__(self):
        self.filepath = None
        self.tiles = None

    def Load(self):
        # Raw text
        text_tiles = np.genfromtxt(self.filepath, delimiter = ',')

        # 2D array of Tile
        self.tiles = np.empty((text_tiles.shape[0], text_tiles.shape[1]), dtype = object)

        # Fill tiles
        for i in range(text_tiles.shape[0]):
            for j in range(text_tiles.shape[1]):
                if text_tiles[i,j] == 0:
                    self.tiles[i,j] = tile.EmptyTile()
                elif text_tiles[i,j] == 1:
                    self.tiles[i,j] = tile.SolidTile()


        # Width, height
        self.w = self.tiles.shape[1]
        self.h = self.tiles.shape[0]
