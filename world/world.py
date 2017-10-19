# Python standard library
import sys

# Game dependent
import entity_manager
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/room/')
import room


class World():
    def __init__(self):
        self.entity_manager = entity_manager.EntityManager()



    def LoadGame(self):

        # Load room
        self.LoadRoom('prototype2')

        # Load entities
        self.entity_manager.CreateEntity('hero', creation_time = 'instant')
        self.entity_manager.CreateEntity('camera', creation_time = 'instant')


        pass

    def LoadRoom(self, room_name):
        if room_name == 'prototype2':
            self.LoadPrototype2Room()

    def LoadPrototype2Room(self):
        # Load the actual room
        self.room = room.Prototype2Room()

        # Set the music for the world
        self.song_file_path = self.room.song_file_path
