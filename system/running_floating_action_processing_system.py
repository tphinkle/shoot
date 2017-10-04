#Python standard library
import sys

# Game specific
sys.path.append('../functions/')
import constants

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

        if entity.running_floating_action.direction == 'left':
            entity.kinematics.sources['running_floating'].ax = constants.infinity

        elif entity.running_floating_action.direction == 'right':
            entity.kinematics.sources['running_floating'].ax = -constants.infinity

        entity.kinematics.sources['running_floating'].target_vx = 0



    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.running_floating_action:

                # Active
                if entity.running_floating_action.status == 'active':

                        # Check run or float
                        if entity.gravity.grounded:
                            self.mode = 'running'
                            self.Run(entity)

                        elif not entity.gravity.grounded:
                            self.mode = 'floating'
                            self.Float(entity)

                # Inactive
                elif entity.running_floating_action.status == 'inactive':

                    pass





    '''
    Running functions
    '''

    def Run(self, entity):

        # Get correct acceleration
        entity.running_floating_action.acceleration = constants.infinity

        # Set target velocity:
        if entity.running_floating_action.direction == 'left':

            if entity.orientation:
                entity.orientation.facing = 'left'

            entity.kinematics.sources['running_floating'].ax = -entity.running_floating_action.acceleration
            entity.kinematics.sources['running_floating'].target_vx = -entity.running_floating_action.running_speed()

        # Run right
        elif entity.running_floating_action.direction == 'right':

            if entity.orientation:
                entity.orientation.facing = 'right'

            entity.kinematics.sources['running_floating'].ax = entity.running_floating_action.acceleration
            entity.kinematics.sources['running_floating'].target_vx = entity.running_floating_action.running_speed()


    '''
    Floating functions
    '''

    def Float(self, entity):

        entity.running_floating_action.acceleration = constants.infinity

        # Float left
        if entity.running_floating_action.direction == 'left':

            if entity.orientation:
                entity.orientation.facing = 'left'

            entity.kinematics.sources['running_floating'].ax = -entity.running_floating_action.acceleration
            entity.kinematics.sources['running_floating'].target_vx = -entity.running_floating_action.running_speed()






        # Float right
        if entity.running_floating_action.direction == 'right':

            if entity.orientation:
                entity.orientation.facing = 'right'

            entity.kinematics.sources['running_floating'].ax = entity.running_floating_action.acceleration
            entity.kinematics.sources['running_floating'].target_vx = entity.running_floating_action.running_speed()
