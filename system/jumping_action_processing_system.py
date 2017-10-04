class JumpingActionProcessingSystem(object):

    def __init__(self):
        pass




    def Trigger(self, entity, args):
        if 'start' in args:
            self.StartAction(entity, args)
        elif 'stop' in args:
            self.StopAction(entity, args)

    def StartAction(self, entity, args):

        # Single jump
        if entity.gravity.grounded == True:
            entity.jumping_action.status = 'active'
            entity.jumping_action.mode = 'single'
            entity.kinematics.vy = entity.jumping_action.speed()
            #entity.kinematics.sources['jumping'].ay = -entity.jumping_action.initial_acceleration

        # Double jump
        elif entity.jumping_action.double_jump_available == True:
            entity.jumping_action.status = 'active'
            entity.jumping_action.mode = 'double'
            entity.jumping_action.double_jump_available = False

    def StopAction(self, entity, args = None):
        entity.jumping_action.status = 'inactive'
        entity.kinematics.sources['jumping'].ay = 0
        entity.jumping_action.timer = 0






    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.jumping_action:



                # Active
                if entity.jumping_action.status == 'active':

                    # Single jump
                    if entity.jumping_action.mode == 'single':

                        # Check timer
                        if entity.jumping_action.timer >= entity.jumping_action.period:
                            self.StopAction()
                            return

                        self.SingleJump(entity, dt)



                    # Double jump
                    elif entity.jumping_action.mode == 'double':
                        # Check timer
                        if entity.jumping_action.timer >= entity.jumping_action.period:
                            self.StopAction()
                            return

                    self.UpdateTimer(entity, dt)


                # Inactive
                elif entity.jumping_action.status == 'inactive':
                    if entity.gravity.grounded == True:
                        entity.jumping_action.double_jump_available = True
                    pass


    def SingleJump(self, entity, dt):

        entity.kinematics.sources['jumping'].ay = -entity.jumping_action.increment_acceleration




    def DoubleJump(self, entity):
        entity.kinematics.ay_sources['jumping'] = entity.jumping_action.acceleration




    def UpdateTimer(self, entity, dt):
        entity.jumping_action.timer += dt
