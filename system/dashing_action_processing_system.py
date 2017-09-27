class DashingActionProcessingSystem(object):

    def __init__(self):
        pass


    def ProcessDashing(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.dashing_action:



                if entity.dashing_action.status == 'triggered':
                    if self.CheckDashValid(entity):
                        entity.dashing_action.status = 'active'
                        self.Dash(entity, dt)

                    else:
                        entity.dashing_action.status = 'inactive'


                elif entity.dashing_action.status == 'active':
                    if not self.CheckDashValid(entity):
                        entity.dashing_action.status = 'inactive'

                    else:
                        self.Dash(entity, dt)


    def CheckDashValid(self, entity):
        if entity.gravity.grounded == True:
            return True

        else:
            return False


    def Dash(self, entity, dt):
        entity.dashing_action.timer += dt

        if entity.dashing_action.timer >= entity.dashing_action.duration:
            self.StopDash(entity)

        else:
            if entity.orientation.facing == 'left':
                entity.kinematics.vx = -entity.dashing_action.speed()
            elif entity.orientation.facing == 'right':
                entity.kinematics.vx = entity.dashing_action.speed()




    def StopDash(self, entity):
        entity.dashing_action.timer = 0.
        entity.dashing_action.status = 'inactive'
