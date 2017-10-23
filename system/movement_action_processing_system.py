# Python standard library
import sys

# Game specific
import helper_systems


class MovementActionProcessingSystem(helper_systems.Subject):

    def __init__(self):

        helper_systems.Subject.__init__(self)

        pass

    def InterpretRawCommand(self, raw_command):
        pass


    def Trigger(self, entity, action):
        pass


    def ProcessAction(self, world, dt):
        pass
