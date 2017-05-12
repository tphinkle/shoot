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

        self.room = room.PrototypeRoom()

        self.entity_manager.CreateHero()
        self.entity_manager.CreateCamera()


        pass
