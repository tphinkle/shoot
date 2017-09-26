# Python standard library
import sys
import itertools
import time

# Scipy
import numpy as np

# Game related
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/functions')
import coord_transforms
import tile_functions

class TilemapCollisionSystem():
    def __init__(self):
        pass


    def ProcessTilemapCollisions(self, world):
        '''
        Main loop for tilemap collision

        1. Move horizontally
            - Check if movement is allowed (if there are obstructions in way or not)
            - If there is an obstruction, move to the correct x-position
        2. Move vertically
            - vy = 0
                - Resolve ramp
            - vy != 0
                - Handle bottom/top collisions

        3. Check grounded
        '''

        tilemap = world.room.tilemap
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.tilemap_collidable != None:

                # X

                if entity.kinematics.vx < 0:
                    self.HandleLeftCollision(entity, tilemap)


                elif entity.kinematics.vx > 0:
                    self.HandleRightCollision(entity, tilemap)

                # Y

                if entity.kinematics.vy == 0:
                    self.ResolveRamp(entity, tilemap)

                if entity.kinematics.vy > 0:
                    self.HandleBottomCollision(entity, tilemap)
                    self.ResolveRamp(entity, tilemap)

                elif entity.kinematics.vy < 0:
                    self.HandleTopCollision(entity, tilemap)
#                    self.ResolveRamp(entity, tilemap)

                self.CheckGrounded(entity, tilemap)







    def HandleLeftCollision(self, entity, tilemap):
        left_x = entity.kinematics.x
        left_proposed_x = entity.kinematics.x_proposed
        top_y = coord_transforms.GetEntityTopY(entity)
        bottom_y = coord_transforms.GetEntityBottomY(entity)

        intersecting_rows = range(int(top_y)/16, int(bottom_y)/16 + 1)
        inbetween_columns = range(int(left_proposed_x)/16, int(left_x)/16 + 1)


        # Loop over columns
        for column in reversed(inbetween_columns):
            # Loop over rows
            for row in intersecting_rows:
                tile = tilemap.tiles[row, column]

                if tile.type == 'solid':

                    # Solid tile doesn't count as obstruction if adjacent tile is ramp
                    if tilemap.tiles[row, column + 1].type == 'ramp':
                        pass

                    # Tile is obstructing; relocate to proper location
                    else:
                        entity.kinematics.x_proposed = (column+1)*16
                        entity.kinematics.vx = 0
                        return

    def HandleRightCollision(self, entity, tilemap):
        x_right = entity.kinematics.x + entity.shape.w
        x_right_proposed = entity.kinematics.x_proposed + entity.shape.w
        top_y = coord_transforms.GetEntityTopY(entity)
        bottom_y = coord_transforms.GetEntityBottomY(entity)

        intersecting_rows = range(int(top_y)/16, int(bottom_y)/16 + 1)
        inbetween_columns = range(int((x_right)/16.), int(x_right_proposed/16. + 1))

        # Loop over columns
        for column in inbetween_columns:
            # Loop over rows
            for row in intersecting_rows:
                tile = tilemap.tiles[row, column]

                # Solid
                if tile.type == 'solid':

                    # Solid tile doesn't count as obstruction if adjacent tile is ramp
                    if tilemap.tiles[row, column-1].type == 'ramp':
                        pass

                    # Tile is obstructing; relocate to proper location
                    else:
                        entity.kinematics.x_proposed = int(16*column - entity.shape.w)
                        entity.kinematics.vx = 0
                        return



    def ResolveRamp(self, entity, tilemap):
        bottomcenter_pixel = coord_transforms.GetEntityBottomCenterPixel(entity)
        bottom_y = coord_transforms.GetEntityBottomY(entity)
        center_x = coord_transforms.GetEntityCenterX(entity)

        tile = tile_functions.GetTile(bottomcenter_pixel, tilemap)
        tile_x = int(center_x - center_x%16)
        tile_y = int(bottom_y - bottom_y%16)



        # Solid
        if tile.type == 'solid':
            entity.kinematics.y_proposed = entity.kinematics.y_proposed-(bottom_y%16+1)
            entity.kinematics.vy = 0
            entity.gravity.grounded = True


        bottomcenter_pixel = coord_transforms.GetEntityBottomCenterPixel(entity)
        bottom_y = coord_transforms.GetEntityBottomY(entity)
        center_x = coord_transforms.GetEntityCenterX(entity)

        tile = tile_functions.GetTile(bottomcenter_pixel, tilemap)
        tile_x = int(center_x - center_x%16)
        tile_y = int(bottom_y - bottom_y%16)

        # Ramp
        if tile.type == 'ramp':
            tile_y = bottom_y - (bottom_y%16)
            floor_y = tile.a + (center_x%16)*(tile.b-tile.a)/16.
            entity.kinematics.y_proposed = entity.kinematics.y_proposed - (bottom_y%16 - floor_y)
            entity.kinematics.vy = 0
            entity.gravity.grounded = True


    def HandleBottomCollision(self, entity, tilemap):
        y_bottom = entity.kinematics.y + entity.shape.h
        y_bottom_proposed = entity.kinematics.y_proposed + entity.shape.h
        x_left = coord_transforms.GetEntityLeftX(entity)
        x_right = coord_transforms.GetEntityRightX(entity)

        intersecting_columns = range(int(x_left/16.), int(x_right)/16 + 1)
        inbetween_rows = range(int(y_bottom)/16, int(y_bottom_proposed)/16 + 1)


        # Loop over rows
        for row in inbetween_rows:
            # Loop over columns
            for column in intersecting_columns:
                if tilemap.tiles[row, column].type == 'solid':
                    entity.kinematics.y_proposed = int(16*row - entity.shape.h)
                    entity.kinematics.vy = 0
                    entity.gravity.grounded = True
        pass

    def HandleTopCollision(self, entity, tilemap):
        y_top = entity.kinematics.y
        y_top_proposed = entity.kinematics.y_proposed
        x_left = coord_transforms.GetEntityLeftX(entity)
        x_right = coord_transforms.GetEntityRightX(entity)

        intersecting_columns = range(int(x_left/16.), int(x_right)/16+1)
        inbetween_rows = range(int(y_top_proposed)/16, int(y_top)/16 + 1)


        # Loop over rows
        for row in inbetween_rows:
            # Loop over columns
            for column in intersecting_columns:
                if tilemap.tiles[row, column].type == 'solid':
                    entity.kinematics.y_proposed = (row + 1)*16
        pass



    def CheckGrounded(self, entity, tilemap):
        belowcenter_pixel = coord_transforms.GetEntityBelowCenterPixel(entity)
        below_y = coord_transforms.GetEntityBelowY(entity)
        center_x = coord_transforms.GetEntityCenterX(entity)

        tile = tile_functions.GetTile(belowcenter_pixel, tilemap)
        tile_x = int(center_x - center_x%16)
        tile_y = int(below_y - below_y%16)

        # Solid
        if tile.type == 'solid':
            entity.kinematics.vy = 0
            entity.gravity.grounded = True

        # Ramp
        elif tile.type == 'ramp':
            bottom_y = coord_transforms.GetEntityBottomY(entity)

            floor_y = tile.a + (center_x%16)*(tile.b-tile.a)/16.+1


            if (int(bottom_y%16) == int(floor_y)-1):
                entity.kinematics.vy = 0
                entity.gravity.grounded = True

            else:
                entity.gravity.grounded = False

        else:
            entity.gravity.grounded = False




    '''



    def ProcessTilemapCollisions(self, world):
        tilemap = world.room.tilemap
        for key, entity in world.entity_manager.entitys.iteritems():


            if entity.tilemap_collidable != None:
                #self.HandleWallCollision(entity, tilemap)
                #self.HandleGroundCollision(entity, tilemap)

                overlap_dimensions = self.GetCollisionOverlapDimensions(entity, tilemap)
                if overlap_dimensions != []:
                    if overlap_dimensions[0] > overlap_dimensions[1]:
                        self.HandleWallCollision(entity, tilemap)
                        self.HandleGroundCollision(entity, tilemap)

                    elif overlap_dimensions[1] <= overlap_dimensions[0]:
                        self.HandleGroundCollision(entity, tilemap)
                        self.HandleWallCollision(entity, tilemap)





    - Write a function that checks all types of overlap tiles first; based
    on the type of overlap titles, different functions will be called.
    - Write a function that first checks if resolving one resolves the other;
    this can determine the update order!



    def GetCollisionOverlapDimensions(self, entity, tilemap):
        pixels = coord_transforms.GetEntityPixels(entity)
        overlap_pixels = np.empty((0,2))
        overlap_dimensions = []
        for pixel in pixels:
            tile = tile_functions.GetTile(pixel, tilemap)
            if tile.type == 'solid':
                overlap_pixels = np.vstack((overlap_pixels, pixel))




        if overlap_pixels.shape[0] > 0:
            overlap_dimensions.append(overlap_pixels[:,0].max()-overlap_pixels[:,0].min())
            overlap_dimensions.append(overlap_pixels[:,1].max()-overlap_pixels[:,1].min())
        print overlap_dimensions
        return overlap_dimensions


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

    '''
