#Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import constants

sys.path.append('../components/')
import kinematics_component

import helper_systems

class RunningFloatingProcessingSystem(helper_systems.Subject):

    def __init__(self):

        # Initialize observer class
        helper_systems.Subject.__init__(self)


        pass




    def Trigger(self, entity, action):
        if action['trigger'] == 'start':
            self.StartAction(entity, action)
        if action['trigger'] == 'stop':
            self.StopAction(entity, action)

    def StartAction(self, entity, action):
        entity.running_floating_action.status = 'active'

        if action['direction'] == 'left':
            entity.running_floating_action.direction = 'left'

        elif action['direction'] == 'right':
            entity.running_floating_action.direction = 'right'

    def StopAction(self, entity, action = None):
        entity.running_floating_action.status = 'inactive'

        #self.Stop(entity)





    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.running_floating_action:

                # Active
                if entity.running_floating_action.status == 'active':

                        # Check run or float
                        if entity.gravity.grounded:
                            entity.running_floating_action.mode = 'running'
                            self.Run(entity)

                        elif not entity.gravity.grounded:
                            entity.running_floating_action.mode = 'floating'
                            self.Float(entity)

                # Inactive
                elif entity.running_floating_action.status == 'inactive':
                    pass




    '''
    Running functions
    '''

    def Stop(self, entity):
        entity.running_floating_action.status = 'inactive'

        pass

    def Run(self, entity):

        # Run left
        if entity.running_floating_action.direction == 'left':
            self.RunLeft(entity)


        # Run right
        elif entity.running_floating_action.direction == 'right':
            self.RunRight(entity)



    def RunLeft(self, entity):
        # Change orientation
        if entity.orientation:
            entity.orientation.xorientation = 'left'


        # Entity is moving left faster than running speed
        if entity.kinematics.vx < -entity.running_floating_action.running_speed():
            return


        # Entity is moving right
        ax = -entity.friction.acceleration
        target_vx = -entity.running_floating_action.running_speed()

        if entity.kinematics.vx < -entity.running_floating_action.running_speed():
            ax = ax*(-1.)

        x_source = kinematics_component.KinematicsXSource(ax, target_vx)
        entity.kinematics.x_sources.append(x_source)



    def RunRight(self, entity):
        if entity.orientation:
            entity.orientation.xorientation = 'right'

        if entity.kinematics.vx > entity.running_floating_action.running_speed():
            return

        ax = entity.friction.acceleration
        target_vx = entity.running_floating_action.running_speed()

        if entity.kinematics.vx > entity.running_floating_action.running_speed():
            ax = ax*(-1.)

        x_source = kinematics_component.KinematicsXSource(ax, target_vx)
        entity.kinematics.x_sources.append(x_source)



    '''
    Floating functions
    '''

    def Float(self, entity):

        entity.running_floating_action.acceleration = constants.infinity

        # Float left
        if entity.running_floating_action.direction == 'left':

            if entity.orientation:
                entity.orientation.xorientation = 'left'

            if entity.kinematics.vx < -entity.running_floating_action.running_speed():
                return

            ax = -entity.running_floating_action.acceleration

            if entity.kinematics.vx == 0:
                target_vx = -entity.running_floating_action.floating_speed()
            elif entity.kinematics.vx != 0:
                target_vx = -abs(entity.kinematics.vx)

            x_source = kinematics_component.KinematicsXSource(ax, target_vx)
            entity.kinematics.x_sources.append(x_source)






        # Float right
        if entity.running_floating_action.direction == 'right':

            if entity.orientation:
                entity.orientation.xorientation = 'right'

            if entity.kinematics.vx > entity.running_floating_action.running_speed():
                return

            ax = entity.running_floating_action.acceleration

            if entity.kinematics.vx == 0:
                target_vx = entity.running_floating_action.floating_speed()
            elif entity.kinematics.vx != 0:
                target_vx = abs(entity.kinematics.vx)

            x_source = kinematics_component.KinematicsXSource(ax, target_vx)
            entity.kinematics.x_sources.append(x_source)
