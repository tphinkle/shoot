# Python standard library
import sys
import itertools

# Program specific
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/functions')
import coord_transforms

class AISystem():
    def __init__(self):
        pass

    def ProcessAI(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.ai != None:
                if entity.ai.behavior == 'following':
                    self.ProcessAI_Following(entity, world)



    def ProcessAI_Following(self, entity, world):
        target = entity.following.target


        target_center_coords = coord_transforms.GetEntityCenterCoords(target)
        #main_camera_center_coords = coord_transforms.GetEntityCenterCoords(main_camera)

        # Target moving right
        if target.velocity.vx > 0:
            if target_center_coords[0] - entity.position.x > entity.following.xlag:
                entity.actions.action_queue.append('PanRight')
            else:
                entity.actions.action_queue.append('PanHorizontalStop')

        # Target moving left
        elif target.velocity.vx < 0:
            if entity.position.x + entity.shape.w - target_center_coords[0] > entity.following.xlag:
                entity.actions.action_queue.append('PanLeft')
            else:
                entity.actions.action_queue.append('PanHorizontalStop')

        # Target stationary (horizontal)
        else:
            entity.actions.action_queue.append('PanHorizontalStop')

        # Target moving Down
        if target.velocity.vy > 0:
            if target_center_coords[1] - entity.position.y > entity.following.ylag:
                entity.actions.action_queue.append('PanDown')
            else:
                entity.actions.action_queue.append('PanVerticalStop')

        # Target moving Up
        elif target.velocity.vx < 0:
            if entity.position.y + entity.shape.h - target_center_coords[1] > entity.following.ylag:
                entity.actions.action_queue.append('PanUp')
            else:
                entity.actions.action_queue.append('PanVerticalStop')

        # Target stationary (vertical)
        else:
            entity.actions.action_queue.append('PanVerticalStop')
