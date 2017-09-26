class JumpingActionProcessingSystem(object):

    def __init__(self):
        pass


    def ProcessJumping(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.jumping_action:
                if entity.jumping_action.active:
                    if self.CheckJumpValid(entity):
                        entity.kinematics.vy = -entity.jumping_action.speed()




                    entity.jumping_action.active = False




    def CheckJumpValid(self, entity):
        if entity.gravity.grounded == True:
            return True

        else:
            return False
