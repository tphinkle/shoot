# Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import coord_transforms
import tile_functions


# Subsystems
import move_action_processing_system
import jump_action_processing_system
import dash_action_processing_system
import shoot_action_processing_system


class ActionsProcessingSystem():
    '''

    '''


    def __init__(self):

        '''
        Sub-systems
        '''
        self.move_action_processing_system = move_action_processing_system.MoveActionProcessingSystem()
        self.jump_action_processing_system = jump_action_processing_system.JumpActionProcessingSystem()
        self.dash_action_processing_system = dash_action_processing_system.DashActionProcessingSystem()
        self.shoot_action_processing_system = shoot_action_processing_system.ShootActionProcessingSystem()


        self.subsystems_map = {}
        self.subsystems_map['move'] = self.move_action_processing_system
        self.subsystems_map['dash'] = self.dash_action_processing_system
        self.subsystems_map['jump'] = self.jump_action_processing_system
        self.subsystems_map['shoot'] = self.shoot_action_processing_system

    def AddObserversToSubsystems(self, observers):
        '''
        Observers are SoundSystem and SpriteAnimationSystem
        They need to be notified upon a state change of their Subject
        '''

        for subsystem in self.subsystems_map.values():
            for observer in observers:
                subsystem.AddObserver(observer)






    def Update(self, world, dt):

        # Trigger actions
        for key, entity in world.entity_manager.entities.iteritems():

            # Process entity actions
            if entity.active != None:

                self.UnpauseEntityActions(entity)

                self.SetEntityTriggers(entity)

                self.CheckEntityInterrupts(entity)

                self.ProcessEntityTriggers(entity)

                self.CheckEntityOverrides(entity)

                self.ProcessEntityActions(entity, world, dt)

                self.ClearEntityCommands(entity)

    def UnpauseEntityActions(self, entity):
        for action in entity.active.actions:
            if action.active_status == 'paused':
                action.active_status = 'active'


    def SetEntityTriggers(self, entity):
        for command in entity.active.commands:
            subsystem = self.subsystems_map[command['action'].action_class]
            subsystem.SetEntityTrigger(entity, command)



    def CheckEntityInterrupts(self, entity):
        # If action A interrupts action B
        # e.g., Move left is triggered while dashing right
        # The Move Left command triggers dashing to stop
        # Set action B to trigger 'stop'
        for command in entity.active.commands:
            if command['action'] == 'start':
                print command
        pass

    def ProcessEntityTriggers(self, entity):
        for action in entity.active.actions:
            subsystem = self.subsystems_map[action.action_class]
            subsystem.ProcessEntityTrigger(entity, world, dt)


    def ClearEntityCommands(self, entity):
        entity.active.commands = []
        entity.active.raw_commands = []

    def CheckEntityOverrides(self, entity):
        # If action A overrides action B
        # Set Action B status to 'pause'


        pass





    def ProcessEntityActions(self, entity, world, dt):
        for action in entity.active.actions:

            subsystem = self.subsystems_map[action.action_class]
            subsystem.ProcessAction(entity, world, dt)




    def GetActionSubsystemFromCommand(self, command):
        action_class = self.subsystems_map[command['action'].action_class]

        return self.subsystems_map[action_class]
