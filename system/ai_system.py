# Python standard library
import sys
import itertools

# Program specific
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/functions')
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
        Horizontal motion
        '''

        # Target moving right
        if target.velocity.vx > 0:
            if target_pixel[0] - entity.position.x > entity.following_ai.xlag:
                entity.actions.action_queue.append('PanRight')
            else:
                entity.actions.action_queue.append('PanHorizontalStop')

        # Target moving left
        elif target.velocity.vx < 0:
            if entity.position.x + entity.shape.w - target_pixel[0] > entity.following_ai.xlag:
                entity.actions.action_queue.append('PanLeft')
            else:
                entity.actions.action_queue.append('PanHorizontalStop')

        # Target stationary (horizontal)
        else:
            entity.actions.action_queue.append('PanHorizontalStop')

        '''
        Vertical motion
        '''

        # Target moving Down
        if target.velocity.vy > 0:
            if target_pixel[1] - entity.position.y > entity.following_ai.ylag:
                entity.actions.action_queue.append('PanDown')
            else:
                entity.actions.action_queue.append('PanVerticalStop')

        # Target moving Up
        elif target.velocity.vy < 0:
            if entity.position.y + entity.shape.h - target_pixel[1] > entity.following_ai.ylag:
                entity.actions.action_queue.append('PanUp')
            else:
                entity.actions.action_queue.append('PanVerticalStop')

        # Target stationary (vertical)
        else:
            entity.actions.action_queue.append('PanVerticalStop')
