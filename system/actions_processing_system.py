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


        self.action_process_map = {}



        # Horizontal motion
        self.action_process_map['MoveLeft'] = self.ProcessMoveLeft
        self.action_process_map['MoveRight'] = self.ProcessMoveRight


        # Dashing action
        self.action_process_map['Dash'] = self.ProcessDash

        # Jumping (jump, double jump, etc.)
        self.action_process_map['Jump'] = self.ProcessJump



        # Panning (cameras)
        self.action_process_map['PanLeft'] = self.ProcessPanLeft
        self.action_process_map['PanRight'] = self.ProcessPanRight
        self.action_process_map['PanUp'] = self.ProcessPanUp
        self.action_process_map['PanDown'] = self.ProcessPanDown
        self.action_process_map['PanHorizontalStop'] = self.ProcessPanHorizontalStop
        self.action_process_map['PanVerticalStop'] = self.ProcessPanVerticalStop



        # Shoot buster

        self.action_process_map['Shoot'] = self.ProcessShootBuster



    def ProcessActions(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():

            # Process entity actions
            if entity.actions != None:
                for action in entity.actions.proposed_actions:
                    self.action_process_map[action](entity, dt)
                self.ClearEntityActions(entity)


        '''
        Action subsystems
        '''

        # Running
        self.running_floating_action_processing_system.ProcessRunningFloating(world)

        # Jumping
        self.jumping_action_processing_system.ProcessJumping(world)

        # Dashing
        self.dashing_action_processing_system.ProcessDashing(world, dt)


    def ClearEntityActions(self, entity):
        entity.actions.proposed_actions = []



    def ProcessMoveLeft(self, entity, dt):
        entity.running_floating_action.active = True
        entity.running_floating_action.direction = 'left'





    def ProcessMoveRight(self, entity, dt):
        entity.running_floating_action.active = True
        entity.running_floating_action.direction = 'right'

    def ProcessDash(self, entity, dt):
        entity.dashing_action.status = 'triggered'
        entity.dashing_action.direction = entity.orientation.facing

    '''
    Jumping actions
    '''

    def ProcessJump(self, entity, dt):
        entity.jumping_action.active = True



    '''
    Panning actions
    '''

    def ProcessPanLeft(self, entity, dt):
        entity.kinematics.vx = -1*entity.panning_action.xspeed

    def ProcessPanRight(self, entity, dt):
        entity.kinematics.vx = entity.panning_action.xspeed

    def ProcessPanUp(self, entity, dt):
        entity.kinematics.vy = -1*entity.panning_action.yspeed

    def ProcessPanDown(self, entity, dt):
        entity.kinematics.vy = entity.panning_action.yspeed

    def ProcessPanHorizontalStop(self, entity, dt):
        entity.kinematics.vx = 0

    def ProcessPanVerticalStop(self, entity, dt):
        entity.kinematics.vy = 0



    '''
    Buster actions
    '''

    def ProcessShootBuster(self, entity, dt):
        pass

    def ProcessChargeBuster(self, entity, dt):
        pass
