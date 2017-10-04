class DashingActionProcessingSystem(object):

    def __init__(self):
        pass



    def Trigger(self, entity, args):
        if 'start' in args:
            self.StartAction(entity, args)
        elif 'stop' in args:
            self.StopAction(entity, args)

    def StartAction(self, entity, args):
        entity.dashing_action.status = 'active'
        entity.kinematics.sources['dashing'].ax = 9999
        if entity.orientation.facing == 'left':
            entity.kinematics.sources['dashing'].target_vx = -entity.dashing_action.speed()
        elif entity.orientation.facing == 'right':
            entity.kinematics.sources['dashing'].target_vx = entity.dashing_action.speed()


    def StopAction(self, entity, args):
        entity.dashing_action.status = 'inactive'
        entity.dashing_action.timer = 0
        entity.kinematics.sources['dashing'].ax = 0





    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.dashing_action:



                # Active
                if entity.dashing_action.status == 'active':

                    # Check timer
                    if entity.dashing_action.timer >= entity.dashing_action.period:
                        self.StopAction()
                        return


                    # Complete the action
                    if self.CheckDashValid(entity):
                        self.UpdateTimer(entity, dt)
                        pass

                    # Action invalid; stop
                    else:
                        self.StopAction()



                # Inactive
                elif entity.dashing_action.status == 'inactive':
                    pass






    def CheckDashValid(self, entity):
        if entity.gravity.grounded == True:
            return True

        else:
            return False


    def StopDash(self, entity):
        entity.dashing_action.timer = 0.
        entity.dashing_action.status = 'inactive'


    def UpdateTimer(self, entity, dt):
        entity.dashing_action.timer += dt
