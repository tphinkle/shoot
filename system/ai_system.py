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



        # DEBUG: Always focus target exactly
        debug = True
        if debug:
            target_x = target.kinematics.x
            target_y = target.kinematics.y

            entity.kinematics.x = target_x - entity.shape.w/2.
            entity.kinematics.y = target_y - entity.shape.h/2.
            return



        if abs(entity.kinematics.x - target.kinematics.x) > 300:
            entity.kinematics.x_proposed = target.kinematics.x


        args = []

        pan = False
        # Target moving right
        if target.kinematics.vx > 0:
            if target_pixel[0] - entity.kinematics.x > entity.following_ai.xlag:
                pan = True
                args.append('right')

        # Target moving left
        elif target.kinematics.vx < 0:
            if entity.kinematics.x + entity.shape.w - target_pixel[0] > entity.following_ai.xlag:
                pan = True
                args.append('left')


        # Target moving Down
        if target.kinematics.vy > 0:
            if target_pixel[1] - entity.kinematics.y > entity.following_ai.ylag:
                pan = True
                args.append('down')


        # Target moving Up
        elif target.kinematics.vy < 0:
            if entity.kinematics.y + entity.shape.h - target_pixel[1] > entity.following_ai.ylag:
                pan = True
                args.append('up')


        # Set 'Start' 'Stop' status
        if pan == True:
            args = ['start'] + args
        elif pan == False:
            args = ['stop'] + args



        entity.actions.proposed_actions.append(['pan', args])
