# Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import constants

sys.path.append('../component/')
import kinematics_component

class FrictionSystem():

    def __init__(self):
        pass


    def ProcessFriction(self, world):

        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.friction:


                if len(entity.kinematics.x_sources) == 0:

                    # Entity stationary
                    if entity.kinematics.vx == 0:
                        return

                    if entity.grounded == True:

                        vx_target = 0

                        # Entity moving right
                        if entity.kinematics.vx > 0:
                            ax = -entity.friction.acceleration

                        # Entity moving left
                        elif entity.kinematics.vx < 0:
                            ax = entity.friction.acceleration

                        x_source = kinematics_component.KinematicsXSource(ax, vx_target)
                        entity.kinematics.x_sources.append(x_source)
