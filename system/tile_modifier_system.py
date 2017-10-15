# Python standard library
import sys

# Functions
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/functions/')
import coord_transforms
import tile_functions



class TileModifierSystem:
    '''
    * Responsible for checking tile behavior of tiles entity is overlapping with.
    '''

    def __init__(self):
        pass

    def ProcessTileModifiers(self, world):
        for key, entity in world.entity_manager.entities.iteritems():


            # Check ground tile interactions
            if entity.gravity:
                if entity.gravity.grounded == True:

                    ground_tile = tile_functions.GetEntityBelowCenterTile(entity, world)
                    ground_tile_properties = ground_tile.special_properties

                    # Check none
                    if ground_tile_properties == []:
                        entity.status.frozen = False

                    # Check ice
                    if ground_tile_properties == 'ice':
                        entity.status.frozen = True


                    # Check fire
                    if ground_tile_properties == 'fire':
                        entity.status.burning = True
