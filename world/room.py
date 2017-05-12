# Python standard library
import sys
import csv

csv.field_size_limit(sys.maxsize)

# Scipy
import numpy as np

# SDL
import sdl2
import sdl2.sdlimage

# Game dependent
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/components/')
import display_component
import shape_component
import tile
import tilemap



class Room():
    def __init__(self):
        self.tilemap_location = None
        pass


class TestRoom(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/resources/rooms/prototype/prototype_room.tmp'
        self.tilemap.Load()

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/resources/rooms/prototype/prototype_room.bmp')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 640, 480)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 640
        self.shape.h = 480

class PrototypeRoom(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/resources/rooms/prototype/prototype_room.tmp'
        self.tilemap.Load()

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/resources/rooms/prototype/prototype_room.bmp')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 1280, 960)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 1280
        self.shape.h = 960
