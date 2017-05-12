# Python standard library
import sys

# Game related
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/functions')
import coord_transforms
import tile_functions

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


    def CheckGrounded(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.gravity != None:
                below_left_pixel = coord_transforms.GetEntityBelowLeftPixel(entity)
                below_right_pixel = coord_transforms.GetEntityBelowRightPixel(entity)

                below_left_tile = tile_functions.GetTile(below_left_pixel, world.room.tilemap)
                below_right_tile = tile_functions.GetTile(below_right_pixel, world.room.tilemap)

                if below_left_tile.type == 'solid' or below_right_tile.type == 'solid':
                    entity.gravity.grounded = True
                else:
                    entity.gravity.grounded = False
