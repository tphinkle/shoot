class RunningFloatingActionProcessingSystem():

    def __init__(self):
        
        pass


    def ProcessRunningFloating(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.running_floating_action:

                # Process action
                if entity.running_floating_action.status == 'triggered':

                    # Check run or float
                    if entity.gravity.grounded:
                        self.ProcessRunning(entity, world)

                    elif not entity.gravity.grounded:
                        self.ProcessFloating(entity, world)





                    # Set inactive
                    entity.running_floating_action.status = 'inactive'




                elif entity.running_floating_action.status == 'inactive':

                    entity.kinematics.vx = 0



    '''
    Running functions
    '''

    def ProcessRunning(self, entity, world):
        self.mode = 'running'

        # Run left
        if entity.running_floating_action.direction == 'left':
            self.ProcessRunningLeft(entity, world)

        # Run right
        elif entity.running_floating_action.direction == 'right':
            self.ProcessRunningRight(entity, world)


    def ProcessRunningLeft(self, entity, world):
        entity.kinematics.vx = -entity.running_floating_action.running_speed()
        if entity.orientation:
            entity.orientation.facing = 'left'



    def ProcessRunningRight(self, entity, world):
        entity.kinematics.vx = entity.running_floating_action.running_speed()
        if entity.orientation:
            entity.orientation.facing = 'right'


    '''
    Floating functions
    '''

    def ProcessFloating(self, entity, world):
        self.mode = 'floating'

        # Float left
        if entity.running_floating_action.direction == 'left':
            self.ProcessFloatingLeft(entity, world)

        # Float right
        if entity.running_floating_action.direction == 'right':
            self.ProcessFloatingRight(entity, world)

    def ProcessFloatingLeft(self, entity, world):
        #entity.kinematics.vx = -entity.running_floating_action.floating_speed()

        if entity.orientation:
            entity.orientation.facing = 'left'

    def ProcessFloatingRight(self, entity, world):
#        entity.kinematics.vx = entity.running_floating_action.floating_speed()
        if entity.orientation:
            entity.orientation.facing = 'right'
