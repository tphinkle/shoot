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
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/components/')
import display_component
import shape_component
import sound_component


import tile
import tilemap




# Base

class Room():
    def __init__(self):
        self.tilemap_location = None
        pass


# Load2

class TestRoom(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype/prototype_room.tmp'
        self.tilemap.Load2()

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype/prototype_room.bmp')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 640, 480)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 640
        self.shape.h = 480

class PrototypeRoom(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype/prototype_room.tmp'
        self.tilemap.Load2()

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype/prototype_room.png')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 1280, 960)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 1280
        self.shape.h = 960

class SimpleRoom(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/simple/simple.tmp'
        self.tilemap.Load2()

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/simple/simple.png')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 640, 480)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 640
        self.shape.h = 480


# Load3

class Prototype2Room(Room):
    def __init__(self):
        self.tilemap = tilemap.TileMap()
        self.tilemap.filepath = '/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype_2/prototype_2.tmp'
        self.tilemap.Load3()

        # Song file
        self.sound = sound_component.SoundComponent()
        song_file_path = '/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype_2/prototype_2.wav'
        self.sound.sound_queue.append(sound_component.AmbientSound(song_file_path))

        self.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/rooms/prototype_2/prototype_2.png')
        self.display.source_rect = sdl2.SDL_Rect(0, 0, 2880, 1760)
        self.display.z = 0

        self.shape = shape_component.ShapeComponent()
        self.shape.w = 2880
        self.shape.h = 1760
