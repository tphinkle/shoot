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

        self.room = room.Prototype2Room()

        self.entity_manager.CreateEntity('hero', creation_time = 'instant')
        self.entity_manager.CreateEntity('camera', creation_time = 'instant')


        pass
