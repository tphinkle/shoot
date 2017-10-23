# Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import coord_transforms
import tile_functions


# Subsystems
import movement_action_processing_system
import jumping_action_processing_system
import dashing_action_processing_system
import shooting_action_processing_system


class ActionsProcessingSystem():
    '''

    '''


    def __init__(self):

        '''
        Sub-systems
        '''
        #self.running_floating_action_processing_system = running_floating_action_processing_system.RunningFloatingActionProcessingSystem()
        self.movement_action_processing_system = movement_action_processing_system.MovementActionProcessingSystem()
        self.jumping_action_processing_system = jumping_action_processing_system.JumpingActionProcessingSystem()
        self.dashing_action_processing_system = dashing_action_processing_system.DashingActionProcessingSystem()
        #self.panning_action_processing_system = panning_action_processing_system.PanningActionProcessingSystem()
        self.shooting_action_processing_system = shooting_action_processing_system.ShootingActionProcessingSystem()


        self.subsystems = []
        self.subsystems.append(self.movement_action_processing_system)
        #self.subsystems.append(self.running_floating_action_processing_system)
        self.subsystems.append(self.jumping_action_processing_system)
        self.subsystems.append(self.dashing_action_processing_system)
        #self.subsystems.append(self.panning_action_processing_system)
        self.subsystems.append(self.shooting_action_processing_system)

        self.action_process_map = {}



        # Horizontal motion
        self.action_process_map['move'] = self.TriggerMove

        # Dashing action
        self.action_process_map['dash'] = self.TriggerDash

        # Jumping (jump, double jump, etc.)
        self.action_process_map['jump'] = self.TriggerJump

        # Panning (cameras)
        #self.action_process_map['pan'] = self.TriggerPan

        # Shoot buster
        self.action_process_map['shoot'] = self.TriggerShoot

    def AddObserversToSubsystems(self, observers):
        '''
        Observers are SoundSystem and SpriteAnimationSystem
        They need to be notified upon a state change of their Subject
        '''

        for subsystem in self.subsystems:
            for observer in observers:
                subsystem.AddObserver(observer)






    def Update(self, world, dt):

        # Trigger actions
        for key, entity in world.entity_manager.entities.iteritems():


            # Process entity actions
            if entity.actions != None:
                self.InterpretRawCommands(entity)
                self.CheckEntityInterrupts(entity)
                self.ProcessCommands(entity)

                self.ClearEntityProposedActions(entity)

                self.CheckEntityOverrides(entity, dt)

                self.ProcessActions(entity, dt)




    def ProcessActions(self, entity):
        for subsystem in self.subsystems:
            subsystem.ProcessAction(entity, dt)

    def GetSubsystem(self, action):
        if action['class'] == 'move':
            return self.running_floating_action_processing_system

        elif action['class'] == 'jump':
            return self.jumping_action_processing_system

        elif action['class'] == 'dash':
            return self.dashing_action_processing_system

        elif action['class'] == 'shoot':
            return self.subsystems.append(self.shooting_action_processing_system)




    def InterpretRawCommands(self, entity):

        commands = []
        for raw_commands in entity.actions.raw_commands:
            subsystem = self.GetSubsystem
            command = subsystem.InterpretRawCommand(entity, raw_command)
            commands.append(command)

        entity.commands = commands



    def CheckEntityOverrides(self, entity):
        # If action A overrides action B
        # Set Action B status to 'latent'


        pass



    def CheckEntityInterrupts(self, entity):
        pass




    def ProcessCommands(self, entity):
        for command in entity.actions.commands:
            self.action_process_map[action['class']](entity, command)



    def ClearEntityCommands(self, entity):
        entity.actions.commands = []
        entity.actions.raw_commands = []



    def TriggerMove(self, entity, command):
        self.movement_action_processing_system.Trigger(entity, command)


    def TriggerDash(self, entity, command):
        self.dashing_action_processing_system.Trigger(entity, command)


    def TriggerJump(self, entity, command):
        self.jumping_action_processing_system.Trigger(entity, command)



    def TriggerShoot(self, entity, command):
        self.shooting_action_processing_system.Trigger(entity, command)
