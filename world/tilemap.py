# Python standard library
import csv

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
        # Tranpose is necessary for some reason; not quite sure why, but it works.
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
        self.h = self.tiles.shape[0]
        self.w = self.tiles.shape[1]

    def Load2(self):
        with open(self.filepath, 'r') as fh:
            reader = csv.reader(fh, delimiter = ',')

            header = reader.next()
            self.h = int(header[1])
            self.w = int(header[0])

            self.tiles = np.empty((self.h, self.w), dtype = object)

            i = 0
            for row in reader:
                j = 0
                for column in row:

                    if column == 'E':
                        self.tiles[i,j] = tile.EmptyTile()

                    elif column == 'S':
                        self.tiles[i,j] = tile.SolidTile()

                    else:
                        left_y = int(column[1:4], 16)
                        right_y = int(column[4:7], 16)
                        #if right_y == 0:
                            #right_y =

                        self.tiles[i,j] = tile.RampTile(left_y, right_y)

                    j += 1

                i += 1

            print header
