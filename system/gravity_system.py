# Python standard library
import sys

# Game related
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/functions')
import coord_transforms

class GravitySystem():
    def   __init__(self):
        pass


    def ProcessGravity(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.gravity != None:
                if entity.gravity.grounded == False:
                    if entity.velocity.vy < entity.gravity.terminal_velocity:
                        entity.acceleration.ay = entity.gravity.g
                    else:
                        entity.acceleration.ay = 0

    '''
    def CheckGrounded(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.gravity != None:
                bottom_left_pixel = coord_transforms.GetEntityBottomLeftPixel(entity)
                bottom_right_pixel = coord_transforms.GetEntityBottomRightPixel(entity)
                entity.gravity.grounded = True
    '''
