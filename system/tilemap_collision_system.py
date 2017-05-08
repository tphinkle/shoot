# Python standard library
import sys
import itertools

# Game related
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/functions')
import coord_transforms
import tile_functions

class TilemapCollisionSystem():
    def __init__(self):
        pass

    def ProcessTilemapCollisions(self, world):
        tilemap = world.room.tilemap
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.tilemap_collidable != None:
                self.HandleGroundCollision(entity, tilemap)

    def HandleGroundCollision(self, entity, tilemap):
        if self.CheckGroundCollision(entity, tilemap):
            self.ResolveGroundCollision(entity, tilemap)

    def CheckGroundCollision(self, entity, tilemap):
        bottom_left_pixel = coord_transforms.GetEntityBottomLeftPixel(entity)
        bottom_right_pixel = coord_transforms.GetEntityBottomRightPixel(entity)
        bottom_left_tile = tile_functions.GetTile(bottom_left_pixel[0], bottom_left_pixel[1], tilemap)
        bottom_right_tile = tile_functions.GetTile(bottom_right_pixel[0], bottom_right_pixel[1], tilemap)


        if bottom_left_tile.type == 'solid' or bottom_right_tile.type == 'solid':
            return True
        else:
            return False

    def ResolveGroundCollision(self, entity, tilemap):
        bottom_y = coord_transforms.GetEntityBottomY(entity)
        entity.position.y = entity.position.y - bottom_y%16
        entity.velocity.vy = 0
