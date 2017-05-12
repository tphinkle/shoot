# Python standard library
import sys
import itertools
import time

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
                self.GetCollisionOverlapDimensions(entity, tilemap)
                self.HandleWallCollision(entity, tilemap)
                self.HandleGroundCollision(entity, tilemap)


    '''
    - Write a function that checks all types of overlap tiles first; based
    on the type of overlap titles, different functions will be called.
    - Write a function that first checks if resolving one resolves the other;
    this can determine the update order!
    '''


    def GetCollisionOverlapDimensions(self, entity, tilemap):
        pass


    def HandleGroundCollision(self, entity, tilemap):

        # Get relevant pixels

        below_left_pixel = coord_transforms.GetEntityBelowLeftPixel(entity)
        below_left_tile = tile_functions.GetTile(below_left_pixel, tilemap)
        below_left_type = below_left_tile.type

        below_right_pixel = coord_transforms.GetEntityBelowRightPixel(entity)
        below_right_tile = tile_functions.GetTile(below_right_pixel, tilemap)
        below_right_type = below_right_tile.type

        below_center_pixel = coord_transforms.GetEntityBelowCenterPixel(entity)
        below_center_tile = tile_functions.GetTile(below_center_pixel, tilemap)
        below_center_type = below_center_tile.type



        # Determine type of colision to resolve, and resolve

        # Empty-empty collision
        if below_left_type == 'empty' and below_right_type == 'empty':
            self.ResolveEmptyEmptyGroundCollision(entity, tilemap, debug = False)

        # Empty-solid collision
        elif below_left_type == 'empty' and below_right_type == 'solid':
            self.ResolveEmptySolidGroundCollision(entity, tilemap, debug = False)

        # Solid-empty collision
        elif below_left_type == 'solid' and below_right_type == 'empty':
            self.ResolveSolidEmptyGroundCollision(entity, tilemap, debug = False)

        # Empty-ramp sloped collision
        elif below_left_type == 'empty' and below_right_type == 'ramp':
            self.ResolveEmptyRampGroundCollision(entity, tilemap, debug = False)

        # Ramp-empty collision
        elif below_left_type == 'ramp' and below_right_type == 'empty':
            self.ResolveRampEmptyGroundCollision(entity, tilemap, debug = False)

        # Solid-ramp collision
        elif below_left_type == 'solid' and below_right_type == 'ramp':
            self.ResolveSolidRampGroundCollision(entity, tilemap, debug = False)

        # Ramp-solid collision
        elif below_left_type == 'ramp' and below_right_type == 'solid':
            self.ResolveRampSolidGroundCollision(entity, tilemap, debug = False)

        # Ramp-ramp collision
        elif below_left_type == 'ramp' and below_right_type == 'ramp':
            self.ResolveRampRampGroundCollision(entity, tilemap, debug = False)

        # Solid-solid collision
        elif below_left_type == 'solid' and below_right_type == 'solid':
            self.ResolveSolidSolidGroundCollision(entity, tilemap, debug = False)




    def ResolveEmptyEmptyGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveEmptySolidGroundCollision(self, entity, tilemap, debug = False):
        bottom_y = coord_transforms.GetEntityBottomY(entity)
        entity.position.y = entity.position.y - (bottom_y+1)%16
        entity.velocity.vy = 0
        entity.gravity.grounded = True
        if debug:
            print 'EmptySolid', entity.position.x, entity.position.y, entity.gravity.grounded
        pass

    def ResolveSolidEmptyGroundCollision(self, entity, tilemap, debug = False):
        bottom_y = coord_transforms.GetEntityBottomY(entity)
        entity.position.y = entity.position.y - (bottom_y+1)%16
        entity.velocity.vy = 0
        entity.gravity.grounded = True
        if debug:
            print 'SolidEmpty', entity.position.x, entity.position.y, entity.gravity.grounded

    def ResolveEmptyRampGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveRampEmptyGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveSolidRampGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveRampSolidGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveRampRampGroundCollision(self, entity, tilemap, debug = False):
        pass

    def ResolveSolidSolidGroundCollision(self, entity, tilemap, debug = False):
        below_y = coord_transforms.GetEntityBelowY(entity)
        entity.position.y = entity.position.y - below_y%16
        entity.velocity.vy = 0
        entity.gravity.grounded = True
        if debug:
            print 'SolidSolid', entity.position.x, entity.position.y, entity.gravity.grounded










    def HandleWallCollision(self, entity, tilemap):

        # Get relevant pixels

        top_adjleft_pixel = coord_transforms.GetEntityTopAdjLeftPixel(entity)
        top_adjleft_tile = tile_functions.GetTile(top_adjleft_pixel, tilemap)
        top_adjleft_type = top_adjleft_tile.type

        bottom_adjleft_pixel = coord_transforms.GetEntityBottomAdjLeftPixel(entity)
        bottom_adjleft_tile = tile_functions.GetTile(bottom_adjleft_pixel, tilemap)
        bottom_adjleft_type = bottom_adjleft_tile.type

        top_adjright_pixel = coord_transforms.GetEntityTopAdjRightPixel(entity)
        top_adjright_tile = tile_functions.GetTile(top_adjright_pixel, tilemap)
        top_adjright_type = top_adjright_tile.type

        bottom_adjright_pixel = coord_transforms.GetEntityBottomAdjRightPixel(entity)
        bottom_adjright_tile = tile_functions.GetTile(bottom_adjright_pixel, tilemap)
        bottom_adjright_type = bottom_adjright_tile.type

        # Check left collisions
        if top_adjleft_type == 'solid' or bottom_adjleft_type == 'solid':
            self.ResolveLeftSolidWallCollision(entity, tilemap, debug = True)

        # Check right collisions
        if top_adjright_type == 'solid' or bottom_adjright_type == 'solid':
            self.ResolveRightSolidWallCollision(entity, tilemap, debug = True)

    def ResolveLeftSolidWallCollision(self, entity, tilemap, debug = False):

        adjleft_x = coord_transforms.GetEntityAdjLeftX(entity)
        print 'before:', entity.position.x, adjleft_x
        entity.position.x = entity.position.x + (16-adjleft_x)%16


        entity.velocity.vx = 0
        if debug:
            print 'LeftSolidWall', entity.position.x, adjleft_x, time.time()

    def ResolveRightSolidWallCollision(self, entity, tilemap, debug = False):
        adjright_x = coord_transforms.GetEntityAdjRightX(entity)
        entity.position.x = entity.position.x - adjright_x%16


        entity.velocity.vx = 0
        if debug:
            print 'RightSolidWall', entity.position.x, entity.position.y
