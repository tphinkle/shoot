#Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import constants

sys.path.append('../components/')
import kinematics_component

class RunningFloatingActionProcessingSystem():

    def __init__(self):

        pass




    def Trigger(self, entity, args):
        if 'start' in args:
            self.StartAction(entity, args)
        elif 'stop' in args:
            self.StopAction(entity, args)

    def StartAction(self, entity, args):
        entity.running_floating_action.status = 'active'

        if 'left' in args:
            entity.running_floating_action.direction = 'left'

        elif 'right' in args:
            entity.running_floating_action.direction = 'right'

    def StopAction(self, entity, args = None):
        entity.running_floating_action.status = 'inactive'

        #self.Stop(entity)





    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
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

        # Get correct acceleration
        entity.running_floating_action.acceleration = constants.infinity

        # Run left
        if entity.running_floating_action.direction == 'left':
            self.RunLeft(entity)


        # Run right
        elif entity.running_floating_action.direction == 'right':
            self.RunRight(entity)



    def RunLeft(self, entity):
        # Change orientation
        if entity.orientation:
            entity.orientation.facing = 'left'


        # Entity is moving left faster than running speed
        if entity.kinematics.vx < -entity.running_floating_action.running_speed():
            return


        # Entity is moving right
        ax = -entity.running_floating_action.acceleration
        target_vx = -entity.running_floating_action.running_speed()

        if entity.kinematics.vx < -entity.running_floating_action.running_speed():
            ax = ax*(-1.)

        x_source = kinematics_component.KinematicsXSource(ax, target_vx)
        entity.kinematics.x_sources.append(x_source)



    def RunRight(self, entity):
        if entity.orientation:
            entity.orientation.facing = 'right'

        if entity.kinematics.vx > entity.running_floating_action.running_speed():
            return

        ax = entity.running_floating_action.acceleration
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
                entity.orientation.facing = 'left'

            if entity.kinematics.vx < -entity.running_floating_action.running_speed():
                return

            ax = -entity.running_floating_action.acceleration
            target_vx = -entity.running_floating_action.floating_speed()
            x_source = kinematics_component.KinematicsXSource(ax, target_vx)
            entity.kinematics.x_sources.append(x_source)






        # Float right
        if entity.running_floating_action.direction == 'right':

            if entity.orientation:
                entity.orientation.facing = 'right'

            if entity.kinematics.vx > entity.running_floating_action.running_speed():
                return

            ax = entity.running_floating_action.acceleration
            target_vx = entity.running_floating_action.floating_speed()
            x_source = kinematics_component.KinematicsXSource(ax, target_vx)
            entity.kinematics.x_sources.append(x_source)
