# Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import coord_transforms
import tile_functions


# Subsystems
import running_floating_action_processing_system
import jumping_action_processing_system
import dashing_action_processing_system
import panning_action_processing_system
import shooting_action_processing_system


class ActionsProcessingSystem():
    '''

    '''


    def __init__(self):

        '''
        Sub-systems
        '''
        self.running_floating_action_processing_system = running_floating_action_processing_system.RunningFloatingActionProcessingSystem()
        self.jumping_action_processing_system = jumping_action_processing_system.JumpingActionProcessingSystem()
        self.dashing_action_processing_system = dashing_action_processing_system.DashingActionProcessingSystem()
        self.panning_action_processing_system = panning_action_processing_system.PanningActionProcessingSystem()
        self.shooting_action_processing_system = shooting_action_processing_system.ShootingActionProcessingSystem()


        self.subsystems = []
        self.subsystems.append(self.running_floating_action_processing_system)
        self.subsystems.append(self.jumping_action_processing_system)
        self.subsystems.append(self.dashing_action_processing_system)
        self.subsystems.append(self.panning_action_processing_system)
        self.subsystems.append(self.shooting_action_processing_system)

        self.action_process_map = {}



        # Horizontal motion
        self.action_process_map['move'] = self.TriggerMove

        # Dashing action
        self.action_process_map['dash'] = self.TriggerDash

        # Jumping (jump, double jump, etc.)
        self.action_process_map['jump'] = self.TriggerJump

        # Panning (cameras)
        self.action_process_map['pan'] = self.TriggerPan

        # Shoot buster
        self.action_process_map['shoot'] = self.TriggerShoot






    def ProcessActions(self, world, dt):

        # Trigger actions
        for key, entity in world.entity_manager.entities.iteritems():
            # Process entity actions
            if entity.actions != None:
                for action in entity.actions.proposed_actions:
                    self.action_process_map[action['action']](entity, action)
                self.ClearEntityProposedActions(entity)



        # Resolve action conflicts



        # Process actions
        for subsystem in self.subsystems:
            subsystem.ProcessAction(world, dt)


    def ClearEntityProposedActions(self, entity):
        entity.actions.proposed_actions = []



    def TriggerMove(self, entity, action):
        self.running_floating_action_processing_system.Trigger(entity, action)


    def TriggerDash(self, entity, action):
        self.dashing_action_processing_system.Trigger(entity, action)



    def TriggerJump(self, entity, action):
        self.jumping_action_processing_system.Trigger(entity, action)




    def TriggerPan(self, entity, action):
        self.panning_action_processing_system.Trigger(entity, action)



    def TriggerShoot(self, entity, action):
        self.shooting_action_processing_system.Trigger(entity, action)
