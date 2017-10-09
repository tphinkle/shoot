# Python standard library
import sys

# Game related
sys.path.append('../functions/')
import constants
import coord_transforms
import tile_functions




import kinematics_component

class GravitySystem():
    def   __init__(self):
        pass


    def ProcessGravity(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.gravity != None:

                entity.grounded = tile_functions.CheckEntityGrounded(world, entity)


                # Falling
                if entity.gravity.grounded == False:

                    ay = entity.gravity.g
                    target_vy = entity.gravity.terminal_velocity
                    #target_vy = constants.infinity
                    y_source = kinematics_component.KinematicsYSource(ay, target_vy)
                    entity.kinematics.y_sources.append(y_source)


                '''
                    # Accelerating
                    if entity.kinematics.vy < entity.gravity.terminal_velocity:

                        entity.kinematics.sources['gravity'].ay = entity.gravity.g
                        entity.kinematics.sources['gravity'].target_vy = entity.gravity.terminal_velocity




                    # Terminal
                    else:

                        entity.kinematics.sources['gravity'].ay = 0




                # Grounded
                elif entity.gravity.grounded == True:


                    entity.kinematics.sources['gravity'].ay = 0
                '''
