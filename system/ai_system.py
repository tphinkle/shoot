# Python standard library
import sys
import itertools

# Program specific
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/functions')
import coord_transforms

class AISystem():
    def __init__(self):
        self.ai_map = {}
        self.ai_map['following'] = self.ProcessAI_Following


    def ProcessAI(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.ai != None:
                for behavior in entity.ai.behaviors:
                    self.ai_map[behavior](entity, world)



    def ProcessAI_Following(self, entity, world):
        target = entity.following_ai.target
        target_pixel = coord_transforms.GetEntityMiddleCenterPixel(target)


        '''
        Lost entity
        '''

        if abs(entity.kinematics.x - target.kinematics.x) > 300:
            entity.kinematics.x_proposed = target.kinematics.x


        '''
        Horizontal motion
        '''


        # Target moving right
        if target.kinematics.vx > 0:
            if target_pixel[0] - entity.kinematics.x > entity.following_ai.xlag:
                entity.actions.proposed_actions.append('PanRight')
            else:
                entity.actions.proposed_actions.append('PanHorizontalStop')

        # Target moving left
        elif target.kinematics.vx < 0:
            if entity.kinematics.x + entity.shape.w - target_pixel[0] > entity.following_ai.xlag:
                entity.actions.proposed_actions.append('PanLeft')
            else:
                entity.actions.proposed_actions.append('PanHorizontalStop')

        # Target stationary (horizontal)
        else:
            entity.actions.proposed_actions.append('PanHorizontalStop')

        '''
        Vertical motion
        '''

        # Target moving Down
        if target.kinematics.vy > 0:
            if target_pixel[1] - entity.kinematics.y > entity.following_ai.ylag:
                entity.actions.proposed_actions.append('PanDown')
            else:
                entity.actions.proposed_actions.append('PanVerticalStop')

        # Target moving Up
        elif target.kinematics.vy < 0:
            if entity.kinematics.y + entity.shape.h - target_pixel[1] > entity.following_ai.ylag:
                entity.actions.proposed_actions.append('PanUp')
            else:
                entity.actions.proposed_actions.append('PanVerticalStop')

        # Target stationary (vertical)
        else:
            entity.actions.proposed_actions.append('PanVerticalStop')
